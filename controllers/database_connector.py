import sqlite3
from sqlite3 import Error


class DatabaseConnector:

    # databases/testgpt.db werkt niet voor mij, verander dit naar je eigen path
    database_file = "/Users/nezirnezirevic/Desktop/wp2-2023-mvc-1e5-nlbl/databases/testgpt.db"
    connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.database_file)
            print("connection success!")
        except Error as error:
            print(error)

        return self.connection


if __name__ == "__main__":
    database = DatabaseConnector()
    database.connect()
