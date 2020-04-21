import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import subprocess
from rq import Queue
from worker import conn

q = Queue(connection=conn)
app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *
from util import run_sub_process

@app.route("/")
def hello():
    return "Hello! To get started, please make a HTTP request following the Github <a href='https://github.com/ericc572/lwc_python_api'>README</a>}"

@app.route("/add")
def add_company():
    name=request.args.get('name')
    revenue=request.args.get('revenue')
    ticker=request.args.get('ticker')
    try:
        company = Company(
            name=name,
            revenue=revenue,
            ticker=ticker
        )
        db.session.add(company)
        db.session.commit()
        return "Company added. Company id={}".format(company.id)
    except Exception as e:
	    return(str(e))

@app.route("/getall")
def get_all():
    try:
        companies=Company.query.all()
        return  jsonify([e.serialize() for e in companies])
    except Exception as e:
	    return(str(e))

@app.route("/get/<id_>")
def get_by_id(id_):
    try:
        company=Company.query.filter_by(id=id_).first()
        return jsonify(company.serialize())
    except Exception as e:
	    return(str(e))

@app.route("/getJobs")
def get_all_jobs():
    try:
        joblistings=JobListing.query.all()
        return  jsonify([e.serialize() for e in joblistings])
    except Exception as e:
	    return(str(e))

@app.route("/getJobs/<company_>")
def get_job_by_company(company_):
    try:
        joblistings=JobListing.query.filter_by(company=company_)
        return jsonify([e.serialize() for e in joblistings])
    except Exception as e:
	    return(str(e))

@app.route("/getJobs/<company_>/total")
def get_company_count(company_):
    try:
        listing_count=JobListing.query.filter_by(company=company_).count()
        return jsonify({"count": listing_count})
    except Exception as e:
	    return(str(e))

@app.route("/getJobs/<company_>/<category_>/count")
def get_company_by_category(company_, category_):
    try:
        listing_count=JobListing.query.filter_by(company=company_, category=category_).count()
        return jsonify({"{category_}": listing_count})
    except Exception as e:
	    return(str(e))

@app.route("/getJobs/<company_>/categories")
def get_all_categories(company_):
    try:
        listings = JobListing.query.filter_by(company=company_)
        categories = listings.with_entities(JobListing.category, func.count(JobListing.category)).group_by(JobListing.category).all()
        return jsonify(dict(categories))
    except Exception as e:
	    return(str(e))

@app.route("/get/jobs/<id_>")
def get_job_id(id_):
    try:
        job_listing=JobListing.query.filter_by(id=id_).first()
        return jsonify(job_listing.serialize())
    except Exception as e:
	    return(str(e))

@app.route('/fetchJobs', methods = ['POST'])
def fetch_jobs_from_scrapy():
    accountName = request.json['accountName']
    print("accountName " + accountName)
    print("enqueuing job....")
    result = q.enqueue(run_sub_process, accountName)
    return {"result": "enqueued job"}, 201

if __name__ == '__main__':
    app.run()
