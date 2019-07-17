from sqlalchemy import and_

from myapp.models import ExchangeRate, db


def get_exchange_rates(currency, date_from, date_to):
    return db.session.query(ExchangeRate).filter(
        and_(
            ExchangeRate.currency_code == currency.upper(),
            ExchangeRate.date >= date_from,
            ExchangeRate.date <= date_to
        )
    ).all()


def get_exchange_rates_dict(currency, date_from, date_to):
    rates = get_exchange_rates(currency, date_from, date_to)
    return [{
        'date': rate.date.strftime('%Y-%m-%d'),
        'rate': rate.rate
    } for rate in rates]


def get_last_exchange_rates():
    last_date = db.session.query(ExchangeRate).order_by(
        ExchangeRate.date.desc()
    ).first()
    if last_date:
        return db.session.query(ExchangeRate).filter(
            ExchangeRate.date == last_date.date
        ).order_by(ExchangeRate.currency_code.asc()).all()
    return []


def get_exchange_rates_history(currency):
    return db.session.query(ExchangeRate).filter(
        ExchangeRate.currency_code == currency.upper()
    ).order_by(ExchangeRate.date.desc()).all()
