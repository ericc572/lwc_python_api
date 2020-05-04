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
        if "director" in title or "dir" in title or "chief" in title or "vp" in title or "president" in title:
            category = "Executive"
        elif "recruiter" in title:
            category = "HumanResources"
        elif "sales" in title or "account executive" in title or "development rep" in title:
            category = "Sales"
        elif "marketer" in title or "marketing" in title or "advertisement" in title:
            category = "Marketing"
        elif "UX" in title or "design" in title:
            category = "Design"
        elif "manager" in title:
            category = "Management"
        elif "engineer" in title or "qa" in title or "it" in title or "software" in title:
            category = "EngineeringOrIT"
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
