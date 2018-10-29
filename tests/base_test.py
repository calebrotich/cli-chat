import os
import unittest
import psycopg2
from app import create_app
from manage import Db
from instance.config import app_config


class CLI_Chat_Base(unittest.TestCase):
    def __init__(self):
        self.app = create_app('testing')
        self.db = Db()
        self.test_client = self.app
        self.db.drop_all()
        self.db.create_tables()
        
    def Setup(self):
        self.app_context = self.app.app_context()

        with self.app_context:
            self.app_context.push()
        
        
    def tearDown(self):
        with self.app_context:
            self.app_context.pop()
            
