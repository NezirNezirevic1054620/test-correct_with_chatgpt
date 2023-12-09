import sqlite3
from sqlite3 import Error


class DatabaseConnector:

    def __init__(self):
        self.connection = None
        self.database_file_path = "databases/testgpt.db"

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.database_file_path, check_same_thread=False)
            print("connection success!")
            return self.connection
        except Error as error:
            print(error)
