import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Link(Base):
    __tablename__ = "Links"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now)