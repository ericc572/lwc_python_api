
from app import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    revenue = db.Column(db.String())
    ticker = db.Column(db.String())
    def __init__(self, name, revenue, ticker):
        self.name = name
        self.revenue = revenue
        self.ticker = ticker

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'revenue': self.revenue,
            'ticker':self.ticker
        }

class JobListing(db.Model):
    __tablename__ = 'joblistings'

    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String()) # eventually a reference to Company
    title = db.Column(db.String())
    timeSincePost = db.Column(db.String())
    category = db.Column(db.String())

    def __init__(self, company, title, timeSincePost, category):
        self.company = company
        self.title = title
        self.timeSincePost = timeSincePost
        self.category = category

    def __repr__(self):
        return "<JobListing: title='%s'" % (self.title)

    def serialize(self):
        return {
            'id': self.id,
            'company': self.company,
            'title': self.title,
            'timeSincePost':self.timeSincePost,
            'category': self.category
        }
