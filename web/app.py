from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig


app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Flask Dockerized'


if __name__ == '__main__':
    app.run()
