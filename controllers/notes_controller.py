from sqlite3 import Error
from controllers.database_connector import DatabaseConnector


class NotesController(DatabaseConnector):
    database = DatabaseConnector()
    cursor = database.connect().cursor()

    @staticmethod
    def select_notes():
        NotesController.database.connect()
        try:
            NotesController.cursor.execute("SELECT * FROM notes")
            NotesController.database.connection.commit()
            notes = NotesController.cursor.fetchall()
            print(notes)
            return notes
        except Error as error:
            print(error)

    @staticmethod
    def insert_notes(title, note_source, is_public, teacher_id, category_id, note):
        NotesController.database.connect()
        try:
            NotesController.cursor.execute("INSERT INTO notes(title, note_source, is_public, teacher_id, category_id, "
                                           "note) VALUES(?, ?, ?, ?, ?, ?)", (title, note_source, is_public, teacher_id,
                                                                              category_id, note))
            NotesController.database.connection.commit()
            return NotesController.cursor.lastrowid
        except Error as error:
            print(error)
