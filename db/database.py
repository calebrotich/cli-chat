import psycopg2
from instance.config import app_config




def create_tables():
        connection_string = app_config['development'].DATABASE_URI
        # print(connection_string)
        db_connection = psycopg2.connect(connection_string)
        cursor = db_connection.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                user_id         SERIAL PRIMARY KEY,
                email           VARCHAR(50) UNIQUE NOT NULL,
                password        VARCHAR(100) UNIQUE NOT NULL,
                role            VARCHAR(50) NOT NULL
        );''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS blacklist(
                tokens           VARCHAR(500) UNIQUE NOT NULL

        );''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS comments(
                comment_id           SERIAL PRIMARY KEY,
                lastLoggedInAt       TIMESTAMP NOT NULL,
                author               VARCHAR(50) UNIQUE NOT NULL

                );''')


        db_connection.commit()
        cursor.close()
        db_connection.close()
