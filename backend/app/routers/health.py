from datetime import datetime
from fastapi import APIRouter, Depends, status
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..database import get_db

router = APIRouter(tags=["Health Check"])

@router.get("/health", status_code=status.HTTP_200_OK)
async def health_check(db: Session = Depends(get_db)):
    """
    Health check endpoint that verifies:
    - Database connectivity
    - Returns service status
    """
    health_status = {
        "status": "healthy",
        "services": {},
        "timestamp": datetime.utcnow().isoformat()
    }
    
    try:
        # Test database connection
        result = db.execute(text("SELECT 1"))
        if result.scalar() == 1:
            health_status["services"]["database"] = "available"
        else:
            health_status["services"]["database"] = "unexpected_response"
            raise Exception("Unexpected database response")
            
    except SQLAlchemyError as e:
        db.rollback()
        health_status.update({
            "status": "unhealthy",
            "error": "database_connection_failed",
            "details": str(e)
        })
        return health_status, status.HTTP_503_SERVICE_UNAVAILABLE
        
    except Exception as e:
        health_status.update({
            "status": "degraded",
            "warning": str(e)
        })
        return health_status, status.HTTP_206_PARTIAL_CONTENT
        
    return health_status