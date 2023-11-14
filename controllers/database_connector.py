import sqlite3
from sqlite3 import Error


class DatabaseConnector:

    # databases/testgpt.db werkt niet voor mij, verander dit naar je eigen path
    database_file = "/Users/nezirnezirevic/Desktop/wp2-2023-mvc-1e5-nlbl/databases/testgpt.db"
    connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.database_file, check_same_thread=False)
            print("connection success!")
            return self.connection
        except Error as error:
            print(error)
