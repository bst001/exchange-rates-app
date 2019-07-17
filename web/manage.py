import json
import os
from datetime import datetime

import click

from myapp.models import *


script_dir = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_DIR_PATH = os.path.join(script_dir, '.download')


def find_files(path, extension='', full_paths=True):
    """Finds files in given directory path (not recurisively)"""
    files = os.listdir(path)
    if extension:
        files = [file for file in files if file.endswith(extension)]
    if full_paths:
        files = [os.path.join(path, file) for file in files]
    return files


def read_json(path):
    with open(path) as f:
        return json.load(f)


@click.group()
def cli():
    pass


@cli.command()
def dropdb():
    db.drop_all()


@cli.command()
def initdb():
    db.create_all()


@cli.command()
def update_rates():
    paths = find_files(DOWNLOAD_DIR_PATH)
    for path in paths:
        data = read_json(path)
        for day in data:
            date = datetime.strptime(day['effectiveDate'], '%Y-%m-%d').date()
            for rate in day['rates']:
                db.session.add(ExchangeRate(
                    currency_code=rate['code'],
                    rate=rate['mid'],
                    date=date
                ))
    db.session.commit()


if __name__ == '__main__':
    cli()
