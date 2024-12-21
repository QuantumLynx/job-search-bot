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

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - [@yourusername](https://twitter.com/yourusername)

Project Link: [https://github.com/yourusername/job-search-bot](https://github.com/yourusername/job-search-bot)
