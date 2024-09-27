import unittest
from src.python.db import Database
from psycopg2 import OperationalError

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = Database(host='localhost', database='postgres', user='postgres', password='secret')

    def test_create_connection_success(self):
        conn = self.db.create_connection()
        self.assertIsNotNone(conn)
        conn.close()

    def test_create_connection_invalid_credentials(self):
        invalid_db = Database(host='localhost', database='postgres', user='invalid', password='wrong_password')
        with self.assertRaises(OperationalError):
            invalid_db.create_connection()

    def test_execute_query(self):
        query = "SELECT 1"
        result = self.db.execute_query(query)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()