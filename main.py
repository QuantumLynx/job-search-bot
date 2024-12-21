from scraper.linkedin_scraper import LinkedInScraper
from filters.job_filter import JobFilter
from notifications.notifier import JobNotifier


def main():
    # Initialize components
    scraper = LinkedInScraper()
    job_filter = JobFilter()
    notifier = JobNotifier()

    # Scrape jobs
    scraper.scrape_jobs("software engineer")

    # Filter jobs
    criteria = {
        "location": "San Francisco",
        "role": "Software Engineer",
        "company": "Google",
    }

    matching_jobs = job_filter.filter_jobs(criteria)

    # Send notifications
    if matching_jobs:
        notifier.send_notification("user@example.com", matching_jobs)


if __name__ == "__main__":
    main()
