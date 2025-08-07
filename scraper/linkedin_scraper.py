from bs4 import BeautifulSoup
import requests
from sqlalchemy.orm import sessionmaker
from database.models import JobListing, engine


class LinkedInScraper:
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def scrape_jobs(self, search_term):
        headers = {"User-Agent": "Mozilla/5.0"}
        url = f"https://www.linkedin.com/jobs/search?keywords={search_term}"

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except requests.RequestException as e:
            # In environments without network access, requests can raise
            # exceptions (e.g., ProxyError). Instead of propagating the
            # exception and crashing the application, gracefully return an
            # empty list so callers can decide how to proceed.
            print(f"Failed to fetch jobs: {e}")
            return []

        soup = BeautifulSoup(response.content, "html.parser")

        jobs = soup.find_all("div", class_="job-card-container")

        results = []
        for job in jobs:
            listing = JobListing(
                title=job.find("h3", class_="job-title").text.strip(),
                company=job.find("h4", class_="company-name").text.strip(),
                location=job.find("span", class_="job-location").text.strip(),
                description=job.find(
                    "div", class_="job-description"
                ).text.strip(),
                url=job.find("a", class_="job-link")["href"],
            )
            self.session.add(listing)
            results.append(listing)

        self.session.commit()
        return results
