from scraper.linkedin_scraper import LinkedInScraper
from filters.job_filter import JobFilter
from notifications.notifier import JobNotifier
import yaml
import os


def main():
    # Initialize components
    scraper = LinkedInScraper()
    job_filter = JobFilter()
    notifier = JobNotifier()

    # Scrape jobs
    scraper.scrape_jobs("software engineer")

    # Load filter criteria from config.yaml

    config_path = os.path.expanduser("~/code/job_search_bot/config.yaml")
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    criteria = config["search_criteria"]

    matching_jobs = job_filter.filter_jobs(criteria)

    # Send notifications
    if matching_jobs:
        notifier.send_notification("user@example.com", matching_jobs)


if __name__ == "__main__":
    main()
