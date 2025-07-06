from fastapi import Request
from sse_starlette.sse import EventSourceResponse
from ..database import get_db
from ..models.issue import Issue
import json
import asyncio

async def issue_event_generator(request: Request, db):
    last_id = 0
    while True:
        if await request.is_disconnected():
            break
            
        # Get new issues since last check
        new_issues = db.query(Issue).filter(Issue.id > last_id).all()
        if new_issues:
            last_id = new_issues[-1].id
            yield {
                "event": "issues_update",
                "data": json.dumps([issue.to_dict() for issue in new_issues])
            }
        
        await asyncio.sleep(1)