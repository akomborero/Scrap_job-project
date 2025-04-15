# Scrap Job Project

This Python script scrapes the latest job listings from [vacancymail.co.zw](https://vacancymail.co.zw/jobs/), extracts relevant details, and saves the top 10 jobs to a CSV file.

## Features
- Scrapes job title, company, location, expiry date, and description
- Saves results to `scraped_data.csv`
- Automates the process using `schedule`
- Logs each scraping event

## Technologies Used
- Python
- BeautifulSoup
- Requests
- Pandas
- Schedule
- Logging

## How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/akomborero/Scrap_job-project.git
   cd Scrap_job-project
