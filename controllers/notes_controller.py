from sqlite3 import Error
from controllers.database_connector import DatabaseConnector


class NotesController(DatabaseConnector):

    database = DatabaseConnector()
    database.connect()

    cursor = database.connection.cursor()

    def select_notes(self):
        sqlite_query = ''' SELECT * FROM notes'''
        try:
            self.cursor.execute(sqlite_query)
            self.database.connection.commit()
            print(self.cursor.fetchall())
        except Error as error:
            print(error)


if __name__ == "__main__":
    a = NotesController()
    a.select_notes()
