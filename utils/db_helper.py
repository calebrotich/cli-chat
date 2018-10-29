import os
import psycopg2

from instance.config import app_config

environment = os.environ['APP_SETTINGS']
DATABASE_URI = app_config[environment].DATABASE_URI


def init_db():
    """Open database connections"""
    conn = psycopg2.connect(DATABASE_URI)
    return conn
