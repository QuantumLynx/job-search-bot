import requests
import pytest
import os
import sys

# Ensure the repository root is on the Python path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scraper.linkedin_scraper import LinkedInScraper


def test_scrape_jobs_handles_request_exception(monkeypatch):
    scraper = LinkedInScraper()

    def mock_get(*args, **kwargs):
        raise requests.RequestException("boom")

    monkeypatch.setattr(requests, "get", mock_get)

    result = scraper.scrape_jobs("anything")
    assert result == []
