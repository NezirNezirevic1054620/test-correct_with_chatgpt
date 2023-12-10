import sqlite3
from pathlib import Path


class NoteModel:
    def __init__(self, database):
        db_path = Path(database)
        if not db_path.exists():
            raise FileNotFoundError(f"Database file {database} does not exist")
        self.dbpath = db_path

    def __get_cursor(self):
        connection = sqlite3.connect(self.dbpath)
        cursor = connection.cursor()
        cursor.row_factory = sqlite3.Row
        return cursor

    def insert_note(self, title, note_source, is_public, teacher_id, category_id, note):
        cursor = self.__get_cursor()
        cursor.execute("INSERT INTO notes(title, note_source, is_public, teacher_id, category_id, "
                       "note) VALUES(?, ?, ?, ?, ?, ?)", (title, note_source, is_public, teacher_id,
                                                          category_id, note))
        cursor.connection.commit()
        return cursor.lastrowid

    def get_all_notes(self, teacher_id):
        cursor = self.__get_cursor()
        cursor.execute(
            "SELECT * FROM notes INNER JOIN categories ON notes.category_id = categories.category_id WHERE teacher_id = " + teacher_id)
        return cursor.fetchall()

    def update_note(self, title, note_source, is_public, teacher_id, category_id, note, note_id):
        cursor = self.__get_cursor()
        cursor.execute(
            "UPDATE notes SET title=(?), note_source=(?), is_public=(?), teacher_id=(?), category_id=(?), note=(?) WHERE note_id=(?)",
            [title, note_source, is_public, teacher_id, category_id, note, note_id])
        cursor.connection.commit()
        return cursor.lastrowid

    def select_note(self, note_id):
        cursor = self.__get_cursor()
        cursor.execute(
            "SELECT * FROM notes INNER JOIN categories ON notes.category_id = categories.category_id INNER JOIN teachers ON notes.teacher_id = teachers.teacher_id WHERE note_id=(?)",
            [note_id])
        cursor.connection.commit()
        return cursor.fetchall()

    def delete_note(self, note_id):
        cursor = self.__get_cursor()
        cursor.execute("DELETE FROM notes WHERE note_id=(?)", [note_id])
        cursor.connection.commit()
        return cursor.fetchall()

