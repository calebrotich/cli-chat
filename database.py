import psycopg2
from instance.config import app_config


class SetupDB(object):
    def __init__(self, config_name):
        #create connection to db
        connection_string = app_config[config_name].DATABASE_URI
        # print(connection_string)
        self.db_connection = psycopg2.connect(connection_string)

        #create cursor
        self.cursor = self.db_connection.cursor()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                user_id         SERIAL PRIMARY KEY,
                email           VARCHAR(50) UNIQUE NOT NULL,
                password        VARCHAR(100) UNIQUE NOT NULL,
                role            VARCHAR(50) NOT NULL
        );''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS blacklist(
                tokens           VARCHAR(500) UNIQUE NOT NULL

        );''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS comments(
                comment_id           SERIAL PRIMARY KEY,
                lastLoggedInAt       TIMESTAMP NOT NULL,
                author               VARCHAR(50) UNIQUE NOT NULL

                );''')


        self.db_connection.commit()
        self.cursor.close()
        self.db_connection.close()
