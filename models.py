
from app import db

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
    datePosted = db.Column(db.String())

    def __init__(self, company, title, datePosted):
        self.company = company
        self.title = title
        self.datePosted = datePosted

    def __repr__(self):
        return "<JobListing: title='%s'" % (self.title)

    def serialize(self):
        return {
            'id': self.id,
            'company': self.company,
            'title': self.title,
            'datePosted':self.datePosted
        }
