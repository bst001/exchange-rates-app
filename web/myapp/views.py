from flask import render_template

from myapp import app
from myapp.exchange_rates import (
    get_exchange_rates_history,
    get_last_exchange_rates,
)

MAX_CHART_RECORDS = 90


@app.route('/')
def last_exchange_rates_view():
    return render_template(
        'home.jinja2',
        rates=get_last_exchange_rates(),
    )


@app.route('/history/<currency>')
def history_exchange_rates_view(currency):
    rates = get_exchange_rates_history(currency)

    chart_dates = []
    chart_rates = []
    chart_length = min(len(rates), MAX_CHART_RECORDS)
    for rate in rates[:chart_length][::-1]:
        chart_dates.append(rate.date.strftime('%Y-%m-%d'))
        chart_rates.append(float(rate.rate))

    return render_template(
        'history.jinja2',
        currency_code=currency.upper(),
        chart_dates=chart_dates,
        chart_rates=chart_rates,
        rates=rates,
    )
