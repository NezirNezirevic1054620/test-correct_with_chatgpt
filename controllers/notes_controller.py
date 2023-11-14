from sqlite3 import Error
from controllers.database_connector import DatabaseConnector


class NotesController:

    @staticmethod
    def select_notes():
        database = DatabaseConnector()
        database.connect()
        cursor = database.connection.cursor()
        try:
            cursor.execute("SELECT * FROM notes")
            database.connection.commit()
            notes = cursor.fetchall()
            print(notes)
            return notes
        except Error as error:
            print(error)

    @staticmethod
    def insert_notes(title, note_source, is_public, teacher_id, category_id, note):
        database = DatabaseConnector()
        database.connect()
        cursor = database.connection.cursor()
        try:
            cursor.execute("INSERT INTO notes(title, note_source, is_public, teacher_id, category_id, "
                           "note) VALUES(?, ?, ?, ?, ?, ?)", (title, note_source, is_public, teacher_id,
                                                              category_id, note))
            database.connection.commit()
            return cursor.lastrowid
        except Error as error:
            print(error)
