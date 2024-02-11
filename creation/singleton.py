import logging
import threading
from typing import Any

import psycopg2


class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs) -> Any:
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance


class DatabaseConnection(Singleton):
    connection: Any

    def __init__(self, host: str, port: int, database: str, user: str, password: str) -> None:
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    def connect(self) -> None:
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password,
            )
            print(f"Connected to the database: {self.database}")
        except psycopg2.Error as e:
            logging.error(f"Error connecting to the database: {str(e)}")
            raise

    def execute_query(self, query: str) -> list[tuple]:
        if self.connection is None or self.connection.closed:
            self.connect()
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            return results
        except psycopg2.Error as e:
            logging.error(f"Error executing query: {str(e)}")
            raise
        finally:
            cursor.close()

    def close_connection(self) -> None:
        if self.connection is not None and not self.connection.closed:
            self.connection.close()
            self.connection = None


if __name__ == "__main__":
    db1 = DatabaseConnection("localhost", 5432, "ekila", "ekila", "ekila")
    db2 = DatabaseConnection("localhost", 5432, "ekila", "ekila", "ekila")

    print(db1 is db2)
    db1.connect()

    query = "SELECT * FROM ekilauth_usermodel"
    results = db2.execute_query(query)
    print(results)
