import datetime
import math
import requests

from myapp.models import ExchangeRate, db


QUERY_URL = 'http://api.nbp.pl/api/exchangerates/tables/{table}/{start_date}/{end_date}/'
QUERY_TABLE_PARAM = 'a'
MAX_DAYS_FOR_SINGLE_QUERY = 93
DAYS = math.ceil(365 / 2)  # ~ half a year


def _get_dates():
    dates = []
    num_of_queries = math.ceil(DAYS/MAX_DAYS_FOR_SINGLE_QUERY)
    end_date = datetime.date.today()

    for n in range(num_of_queries):
        start_date = end_date - datetime.timedelta(days=MAX_DAYS_FOR_SINGLE_QUERY)
        dates.append({
            'end': end_date,
            'start': start_date
        })
        end_date = start_date - datetime.timedelta(days=1)

    return dates


def _get_download_urls():
    return [
        QUERY_URL.format(
            table=QUERY_TABLE_PARAM,
            start_date=date['start'],
            end_date=date['end']
        ) for date in _get_dates()
    ]


def download_nbp_rates():
    for url in _get_download_urls():
        response = requests.get(url)
        yield response.json()


def download_initial_nbp_rates_and_update_db():
    # TODO: error handling
    for data in download_nbp_rates():
        for day in data:
            date = datetime.datetime.strptime(day['effectiveDate'], '%Y-%m-%d').date()
            for rate in day['rates']:
                db.session.add(ExchangeRate(
                    currency_code=rate['code'],
                    rate=rate['mid'],
                    date=date
                ))
        db.session.commit()


def should_update_rates():
    # TODO: implement & use this or something else (e.g. cron)
    pass


def update_rates():
    # TODO: download only new/missing rates
    pass
