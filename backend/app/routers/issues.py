from fastapi import Request
from sse_starlette.sse import EventSourceResponse
import json
import asyncio

@router.get("/events")
async def issue_events(request: Request, db: Session = Depends(get_db)):
    async def event_generator():
        last_id = 0
        while True:
            if await request.is_disconnected():
                break

            new_issues = db.query(Issue).filter(Issue.id > last_id).all()
            if new_issues:
                last_id = new_issues[-1].id
                yield {
                    "event": "issues_update",
                    "data": json.dumps([
                        {
                            "id": issue.id,
                            "title": issue.title,
                            "status": issue.status,
                        }
                        for issue in new_issues
                    ]),
                }

            await asyncio.sleep(1)

    return EventSourceResponse(event_generator())