import click
from flask.cli import with_appcontext
from models import db

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Inicializa la base de datos."""
    db.create_all()
    print("Base de datos inicializada.")
