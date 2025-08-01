from sqlalchemy import Column, Integer, String, Boolean
from .base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    role = Column(String, default="REPORTER")  # ADMIN, MAINTAINER, REPORTER
    is_active = Column(Boolean, default=True)