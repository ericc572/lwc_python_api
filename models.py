
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
