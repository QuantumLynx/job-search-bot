from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class JobListing(Base):
    __tablename__ = "job_listings"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    company = Column(String)
    location = Column(String)
    description = Column(String)
    url = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


engine = create_engine("sqlite:///jobs.db")
Base.metadata.create_all(engine)
