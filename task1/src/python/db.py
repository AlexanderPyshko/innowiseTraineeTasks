import psycopg2
from psycopg2 import OperationalError
import logging

class Database:
    def __init__(self, host='localhost', database='postgres', user=None, password=None):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def __enter__(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            logging.info("Connected to database successfully")
            return self.conn.cursor()
        except OperationalError as e:
            logging.error(f'Failed to connect to the database: {e}')
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            if exc_type is None:
                self.conn.commit()
                logging.info("Transaction committed")
            else:
                self.conn.rollback()
                logging.error("Transaction rolled back due to error")
            self.conn.close()

    def execute_query(self, query, params=()):
        with self as cursor:
            if cursor:
                try:
                    cursor.execute(query, params)
                except Exception as e:
                    logging.error(f'Query failed: {e}')