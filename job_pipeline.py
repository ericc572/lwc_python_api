import json
import os

from app import db
from models import *
jobFile = 'data.json'
if (os.path.getsize(jobFile) > 0):
    json_file = open(jobFile,'r')
    data = json.load(json_file)
    for p in data:
        title = p['title']
        company = p['company']
        timeSincePost = p['timeSincePost']
        title = title.lower()
        # Manually check and assign categories based on string check
        if "engineer" in title or "qa" in title or "it" in title or "software" in title:
            category = "Engineering"
        elif "sales" in title or "account" in title or "marketing" in title:
            category = "Sales/Marketing"
        elif "UX" in title or "design" in title:
            category = "Design"
        elif "Manager" in title:
            category = "Management, Product"
        else:
            category = "Other"
            # refactor: run ML script

        job_listing = JobListing(
            title=title,
            company=company,
            timeSincePost=timeSincePost,
            category=category
        )
        db.session.add(job_listing)
        db.session.commit()
        print("job listing added. Job id={}".format(job_listing.id))
