from flask import Flask
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from redis import Redis

from myapp.config import BaseConfig


app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)
redis = Redis(
    host=app.config['REDIS_HOST'],
    port=app.config['REDIS_PORT']
)
cache = Cache(app)


import myapp.api
import myapp.views


if __name__ == '__main__':
    app.run()
