import click

from myapp import db
from myapp.external import download_initial_nbp_rates_and_update_db


@click.group()
def cli():
    pass


@cli.command()
def dropdb():
    db.drop_all()


@cli.command()
def initdb():
    db.create_all()
    download_initial_nbp_rates_and_update_db()


if __name__ == '__main__':
    cli()
