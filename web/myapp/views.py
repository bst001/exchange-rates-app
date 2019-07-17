from flask import render_template

from myapp import app
from myapp.exchange_rates import (
    get_exchange_rates_history,
    get_last_exchange_rates,
)


@app.route('/')
def last_exchange_rates_view():
    return render_template(
        'home.jinja2',
        rates=get_last_exchange_rates(),
    )


@app.route('/history/<currency>')
def history_exchange_rates_view(currency):
    return render_template(
        'history.jinja2',
        currency_code=currency.upper(),
        rates=get_exchange_rates_history(currency),
    )
