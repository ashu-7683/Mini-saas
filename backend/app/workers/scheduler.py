from apscheduler.schedulers.background import BackgroundScheduler
from ..database import SessionLocal
from ..models.issue import Issue
from ..models.stats import DailyStats
from datetime import datetime, timedelta
import logging

logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

def aggregate_issue_stats():
    db = SessionLocal()
    try:
        today = datetime.utcnow().date()
        stats = {
            'open': db.query(Issue).filter(Issue.status == 'OPEN').count(),
            'triaged': db.query(Issue).filter(Issue.status == 'TRIAGED').count(),
            'in_progress': db.query(Issue).filter(Issue.status == 'IN_PROGRESS').count(),
            'done': db.query(Issue).filter(Issue.status == 'DONE').count(),
        }
        
        daily_stat = db.query(DailyStats).filter(DailyStats.date == today).first()
        if not daily_stat:
            daily_stat = DailyStats(date=today)
            db.add(daily_stat)
        
        daily_stat.open_count = stats['open']
        daily_stat.triaged_count = stats['triaged']
        daily_stat.in_progress_count = stats['in_progress']
        daily_stat.done_count = stats['done']
        
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        aggregate_issue_stats,
        'interval',
        minutes=30,
        next_run_time=datetime.now() + timedelta(seconds=10)
    scheduler.start()