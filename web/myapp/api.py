from flask import jsonify

from myapp import app, cache
from myapp.exchange_rates import get_exchange_rates_dict


@app.route('/api/exchange-rates/<currency>/<date_from>/<date_to>')
@cache.memoize()
def exchange_rate_resource(currency, date_from, date_to):
    return jsonify(get_exchange_rates_dict(currency, date_from, date_to))
