# Job Search Bot

An automated job search bot that scrapes job listings from LinkedIn and other job boards.

## Features

- Automated login and job searching on LinkedIn
- Database storage of job listings
- Configurable search criteria

## Setup

1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Create a .env file with your credentials:
```
LINKEDIN_EMAIL=your_email
LINKEDIN_PASSWORD=your_password
DB_CONNECTION=sqlite:///jobs.db
```

3. Run the scraper:
```bash
python linkedin_scraper.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.