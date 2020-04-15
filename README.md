# lwc_python_api: Job Scraper for LinkedIn
A very lightweight Flask API for scrapy. Will eventually be hit by a lwc (Lightning web component in salesforce). It calls a scraper, scrapes the job postings on LinkedIn for a particular company, and writes it to a Postgres DB hosted on heroku.

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

# How to scrape data and seed db
Do:

`scrapy crawl linkedin_spider -a accountName=GoDaddy -o ../data.json ` calls linkedin_spider and passes in accountName = GoDaddy, and writes it to data.json
run `python job_pipeline.py`
