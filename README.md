# Job Search Bot

A Python bot that automatically scrapes job listings from LinkedIn, filters them based on your criteria, and sends email notifications for matching positions.

## Features

- LinkedIn job scraping using BeautifulSoup
- Intelligent job filtering with NLP
- Email notifications via SendGrid
- SQLite database for job storage
- Customizable search criteria

## Prerequisites

- Python 3.8+
- SendGrid account and API key
- pip package manager

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/job-search-bot.git
cd job-search-bot
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment:
```bash
cp .env.example .env
# Edit .env and add your SendGrid API key
```

## Configuration

Edit the `.env` file with your settings:
```plaintext
SENDGRID_API_KEY=your_api_key_here
```

### Filter Configuration

Create or edit `config.yaml` to set up your job search filters:
```yaml
search_criteria:
  keywords: ["python", "software engineer"]
  location: "San Francisco, CA"
  experience_level: "Entry Level"
  job_type: "Full-time"

filters:
  salary:
    min: 80000
    max: 150000
    currency: "USD"
  
  required_skills:
    - python
    - sql
    - git
  
  exclude_keywords:
    - senior
    - lead
    - manager
  
  company_blacklist:
    - "Company Name 1"
    - "Company Name 2"
  
  remote_only: true
  posted_within_days: 7
```

The bot will automatically filter jobs based on these criteria.

## Usage

1. Set your job search criteria in `config.yaml`:
```yaml
search_criteria:
  keywords: ["python", "software engineer"]
  location: "San Francisco, CA"
  experience_level: "Entry Level"
  job_type: "Full-time"
```

2. Run the bot:
```bash
python main.py
```

3. The bot will:
   - Scrape LinkedIn jobs matching your criteria
   - Filter results based on your preferences
   - Store new jobs in the SQLite database
   - Send email notifications for new matches

4. Schedule automatic runs (optional):
   - Linux/Mac (using cron):
     ```bash
     # Run every 6 hours
     0 */6 * * * cd /path/to/job_search_bot && ./venv/bin/python main.py
     ```
   - Windows (using Task Scheduler):
     - Create a new task
     - Program: path\to\venv\Scripts\python.exe
     - Arguments: path\to\job_search_bot\main.py
     - Set trigger for desired schedule

## Project Structure

```
job_search_bot/
├── database/        # Database models and operations
├── scraper/         # Job scraping functionality
├── filters/         # Job filtering logic
├── notifications/   # Email notification system
└── main.py         # Main application entry point
```

