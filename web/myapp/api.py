import datetime

from flask import jsonify

from myapp import app, cache


@app.route('/api/<currency>')
@cache.memoize()
def cached_resource(currency):
    value = datetime.datetime.now()
    return jsonify(value)


@app.route('/api/clear-cache')
def clear_cache_resource():
    cache.clear()
    return jsonify('done!')
