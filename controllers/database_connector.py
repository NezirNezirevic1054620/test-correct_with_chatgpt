import sqlite3
from sqlite3 import Error


class DatabaseConnector:

    database_file = "testgpt.db"
    connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.database_file)
            print("connection success!")
        except Error as error:
            print(error)


if __name__ == "__main__":
    database = DatabaseConnector()
    database.connect()
