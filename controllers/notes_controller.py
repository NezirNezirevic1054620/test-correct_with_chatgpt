from sqlite3 import Error
from controllers.database_connector import DatabaseConnector


class NotesController(DatabaseConnector):
    database = DatabaseConnector()
    cursor = database.connect().cursor()

    @staticmethod
    def select_notes():
        NotesController.database.connect()
        try:
            NotesController.cursor.execute("SELECT * FROM notes INNER JOIN categories ON notes.category_id = "
                                           "categories.category_id")
            NotesController.cursor.connection.commit()
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
            NotesController.cursor.connection.commit()
            return NotesController.cursor.lastrowid
        except Error as error:
            print(error)

    @staticmethod
    def delete_note(note_id):
        NotesController.database.connect()
        try:
            NotesController.cursor.execute("DELETE FROM notes WHERE note_id="+note_id)
            NotesController.cursor.connection.commit()

        except Error as error:
            print(error)

    @staticmethod
    def edit_note(note_id):
        NotesController.database.connect()
        try:
            NotesController.cursor.execute("DELETE FROM notes WHERE note_id=" + note_id)
            NotesController.cursor.connection.commit()

        except Error as error:
            print(error)

