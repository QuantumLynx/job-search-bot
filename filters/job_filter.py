import nltk
from nltk.tokenize import word_tokenize
from sqlalchemy.orm import sessionmaker
from database.models import JobListing, engine


class JobFilter:
    def __init__(self, session=None):
        if session is None:
            Session = sessionmaker(bind=engine)
            self.session = Session()
        else:
            self.session = session
        nltk.download("punkt")

    def filter_jobs(self, criteria):
        query = self.session.query(JobListing)

        if "location" in criteria:
            query = query.filter(
                JobListing.location.ilike(f"%{criteria['location']}%")
            )

        if "role" in criteria:
            query = query.filter(
                JobListing.title.ilike(f"%{criteria['role']}%")
            )

        if "company" in criteria:
            query = query.filter(
                JobListing.company.ilike(f"%{criteria['company']}%")
            )

        return query.all()
