from sqlalchemy.ext.declarative import declarative_base

from myapp import db

Base = declarative_base()


class ExchangeRate(db.Model):
    __tablename__ = 'exchange_rates'
    id = db.Column(db.Integer, primary_key=True)
    currency_code = db.Column(db.String(), index=True)
    rate = db.Column(db.String())
    date = db.Column(db.Date(), index=True)
