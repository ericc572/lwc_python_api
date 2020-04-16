import json
import os

from app import db
from models import *

with open('data.json') as json_file:
    data = json.load(json_file)
    for p in data:
        title = p['title']
        company = p['company']
        timeSincePost = p['timeSincePost']
        category = ""#p['category']

        job_listing = JobListing(
            title=title,
            company=company,
            timeSincePost=timeSincePost,
            category=category
        )
        db.session.add(job_listing)
        db.session.commit()
        print("job listing added. Job id={}".format(job_listing.id))
