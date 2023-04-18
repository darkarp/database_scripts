import psycopg2
from config import DB_CONFIG


class Database:
    def __init__(self, db_config):
        self.connection = psycopg2.connect(**db_config)

    def execute_query(self, query):
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
        return results

    def close(self):
        self.connection.close()
