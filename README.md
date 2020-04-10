# lwc_python_api: Job Scraper for LinkedIn
LWC hackathon python flask app. It calls a scraper, scrapes the job postings on LinkedIn for a particular company, and writes it to a Postgres DB hosted on heroku.

## App Info
Visit app at `lwc-python-api.herokuapp.com`

## Current Endpoints Supported
- GET / do nothing
- POST company: `/add?name=Apple&revenue=1370000&ticker=AAPL`
- GET all companies: `/getall` 
- GET all job listings: `/getJobs`
- GET job listings per company: `/getJobs/<company_name>`
- GET job by ID: `/get/jobs/<_id>`
- TODO: Get total count of company job listings: `/getJobs/<company_name>/count`
- TODO: Get count of company job listings by category: `/getJobs/<company_name>/<category>/count `

# How to call scraper 
Do:

`scrapy crawl linkedin_spider` calls linkedin_spider.py
