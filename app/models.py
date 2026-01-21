import datetime

from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime

from database import Base


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(Text)
    done = Column(Boolean)
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now())
