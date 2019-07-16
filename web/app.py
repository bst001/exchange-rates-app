import datetime
from config import BaseConfig
from flask import (
    Flask,
    jsonify,
    render_template,
)
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from redis import Redis


app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)
redis = Redis(
    host=app.config['REDIS_HOST'],
    port=app.config['REDIS_PORT']
)
cache = Cache(app)


@app.route('/')
def hello_world():
    redis.incr('hits')
    total_hits = redis.get('hits').decode()
    return 'Flask Dockerized. Hits: {}.'.format(total_hits)


@app.route('/s')
def page_with_static():
    return render_template('home.jinja2')


@app.route('/api/<currency>')
@cache.memoize()
def cached_resource(currency):
    value = datetime.datetime.now()
    return jsonify(value)


@app.route('/api/clear-cache')
def clear_cache_resource():
    cache.clear()
    return jsonify('done!')


if __name__ == '__main__':
    app.run()
