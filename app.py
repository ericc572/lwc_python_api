import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *

@app.route("/")
def hello():
    return "Hello World!"

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

@app.route("/get/jobs/<id_>")
def get_job_id(id_):
    try:
        job_listing=JobListing.query.filter_by(id=id_).first()
        return jsonify(job_listing.serialize())
    except Exception as e:
	    return(str(e))

if __name__ == '__main__':
    app.run()
