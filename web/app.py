from config import BaseConfig
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import Redis


app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)
redis = Redis(
    host=app.config['REDIS_HOST'],
    port=app.config['REDIS_PORT']
)


@app.route('/')
def hello_world():
    redis.incr('hits')
    total_hits = redis.get('hits').decode()
    return 'Flask Dockerized. Hits: {}.'.format(total_hits)


if __name__ == '__main__':
    app.run()
