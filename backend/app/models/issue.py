from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.sql import func
from .base import Base
from datetime import datetime

class Issue(Base):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    severity = Column(Enum("LOW", "MEDIUM", "HIGH", "CRITICAL", name="severity_levels"))
    status = Column(Enum("OPEN", "TRIAGED", "IN_PROGRESS", "DONE", name="issue_status"), default="OPEN")
    reporter_id = Column(Integer, ForeignKey("users.id"))
    maintainer_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    file_path = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())