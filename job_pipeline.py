import json
import os

from app import db
from models import *

with open('data.json') as json_file:
    data = json.load(json_file)
    for p in data:
        title = p['title']
        company = p['company']
        datePosted = p['timeSincePost']
        # print('Title: ' + p['title'])
        # print('Company: ' + p['company'])
        # print('DatePosted: ' + p['timeSincePost'])
        # print('')
        job_listing = JobListing(
            title=title,
            company=company,
            datePosted=datePosted
        )
        db.session.add(job_listing)
        db.session.commit()
        print("job listing added. Job id={}".format(job_listing.id))
