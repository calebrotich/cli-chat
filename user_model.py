from datetime import datetime, timedelta
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import BadRequest, NotFound, Unauthorized, Forbidden
import psycopg2
from flask import current_app

# Local Imports
# from .instance.config import key as secret_key
from utils.db_helper import init_db


class User():
    """This class contains the functions of the user model"""
    password = ''

    def __init__(self, password='pass', email='mail@mail.com', role='normal'):
        """initialize the user model"""

        User.password = generate_password_hash(password)
        self.email = email
        self.role = role
        self.db = init_db()

    def save_user(self):
        """Saves User Object to Database"""

        new_user = dict(
            role=self.role,
            email=self.email,
            password=self.password,
        )
        # check if user exists
        if self.check_if_user_exists(new_user['email']):
            raise Forbidden("User already exists.Please log in")

        curr = self.db.cursor()

        sql = """INSERT INTO users (role,email,  password) \
            VALUES ( %(role)s, %(email)s, %(password)s);
            """
        curr.execute(sql, new_user)
        self.db.commit()
        curr.close()

    def check_if_user_exists(self, email):
        database = self.db
        curr = database.cursor()
        curr.execute("select * from users where email = (%s);", (email,))
        result = curr.fetchone()
        if result:
            return True
        return False

    def get_user_by_email(self, email):
        """return user from the db given an email"""
        curr = self.db.cursor()
        curr.execute(
            "SELECT role, password, registered_on FROM users WHERE email = (%s);", (email,))
        data = curr.fetchone()
        curr.close()
        return data

   