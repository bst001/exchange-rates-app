from flask import render_template

from myapp import app, redis


@app.route('/')
def hello_world():
    redis.incr('hits')
    total_hits = redis.get('hits').decode()
    return 'Flask Dockerized. Hits: {}.'.format(total_hits)


@app.route('/s')
def page_with_static():
    return render_template('home.jinja2')
