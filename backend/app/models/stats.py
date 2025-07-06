from sqlalchemy import Column, Integer, Date
from .base import Base

class DailyStats(Base):
    __tablename__ = "daily_stats"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, unique=True, nullable=False)
    open_count = Column(Integer, default=0)
    triaged_count = Column(Integer, default=0)
    in_progress_count = Column(Integer, default=0)
    done_count = Column(Integer, default=0)