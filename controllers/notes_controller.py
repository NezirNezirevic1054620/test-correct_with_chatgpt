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
            NotesController.cursor.execute("DELETE FROM notes WHERE note_id=" + note_id)
            NotesController.cursor.connection.commit()

        except Error as error:
            print(error)

    @staticmethod
    def select_note(note_id):
        NotesController.database.connect()
        try:
            NotesController.cursor.execute(
                "SELECT * FROM notes INNER JOIN categories ON notes.category_id = categories.category_id INNER JOIN teachers ON notes.teacher_id = teachers.teacher_id WHERE note_id=" + note_id)
            NotesController.cursor.connection.commit()
            return NotesController.cursor.fetchall()
        except Error as error:
            print(error)

    @staticmethod
    def edit_note(title, note_source, is_public, teacher_id, category_id, note, note_id):
        NotesController.database.connect()
        try:
            NotesController.cursor.execute(
                "UPDATE notes SET title='" + title + "', note_source='" + note_source + "', is_public='" + is_public + "', teacher_id='" + teacher_id + "', category_id='" + category_id + "', is_public='" + is_public + "', note='" + note + "' WHERE note_id=" + note_id)

            NotesController.cursor.connection.commit()
            return NotesController.cursor.fetchall()
        except Error as error:
            print(error)

    @staticmethod
    def search_note(search_value):
        NotesController.database.connect()
        try:
            NotesController.cursor.execute("SELECT * FROM notes INNER JOIN categories ON notes.category_id = "
                                           "categories.category_id WHERE title LIKE (?) OR note LIKE (?)",
                                           ["%" + search_value + "%", "%" + search_value + "%"])
            NotesController.cursor.connection.commit()
            note = NotesController.cursor.fetchall()
            print(note)
            return note
        except Error as error:
            print(error)

    @staticmethod
    def filter_notes(filter_value):
        NotesController.database.connect()
        try:
            NotesController.cursor.execute(
                "SELECT * FROM notes INNER JOIN categories ON notes.category_id = categories.category_id WHERE notes.category_id = " + filter_value)
            NotesController.cursor.connection.commit()
            note = NotesController.cursor.fetchall()
            print(note)
            return note
        except Error as error:
            print(error)
