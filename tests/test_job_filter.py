import os
import sys
from unittest.mock import patch

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Ensure the repository root is on the Python path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.models import Base, JobListing
from filters.job_filter import JobFilter


def setup_in_memory_db():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    jobs = [
        JobListing(
            title="Software Engineer",
            company="OpenAI",
            location="San Francisco",
            description="",
            url="",
        ),
        JobListing(
            title="Data Scientist",
            company="Google",
            location="New York",
            description="",
            url="",
        ),
        JobListing(
            title="Product Manager",
            company="Facebook",
            location="San Francisco",
            description="",
            url="",
        ),
    ]

    session.add_all(jobs)
    session.commit()
    return session


def test_filter_jobs_by_criteria():
    session = setup_in_memory_db()

    with patch("nltk.download"):
        job_filter = JobFilter(session=session)

    results = job_filter.filter_jobs({"location": "San Francisco"})
    assert len(results) == 2
    assert {job.title for job in results} == {"Software Engineer", "Product Manager"}

    results = job_filter.filter_jobs({"role": "Data Scientist"})
    assert len(results) == 1
    assert results[0].company == "Google"

    results = job_filter.filter_jobs({"company": "OpenAI"})
    assert len(results) == 1
    assert results[0].title == "Software Engineer"
