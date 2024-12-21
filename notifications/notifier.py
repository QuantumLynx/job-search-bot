from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os
from dotenv import load_dotenv

load_dotenv()


class JobNotifier:
    def __init__(self):
        self.sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))

    def send_notification(self, email, jobs):
        job_listings = "\n".join(
            [
                f"Title: {job.title}\nCompany: {job.company}\nLocation: {job.location}\nURL: {job.url}\n"
                for job in jobs
            ]
        )

        message = Mail(
            from_email="your-email@example.com",
            to_emails=email,
            subject="New Job Matches Found",
            plain_text_content=f"New jobs matching your criteria:\n\n{job_listings}",
        )

        self.sg.send(message)
