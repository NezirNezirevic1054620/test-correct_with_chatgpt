"""Note Model with all its SQL queries"""
import sqlite3
from pathlib import Path


class NoteModel:
    """NoteModel class with all its methods"""

    def __init__(self, database):
        db_path = Path(database)
        if not db_path.exists():
            raise FileNotFoundError(f"Database file {database} does not exist")
        self.dbpath = db_path

    def __get_cursor(self):
        """Connection with database is made and cursor object gets returned"""
        connection = sqlite3.connect(self.dbpath)
        cursor = connection.cursor()
        cursor.row_factory = sqlite3.Row
        return cursor

    def insert_note(self, title, note_source, is_public, teacher_id, category_id, note):
        """Note row gets inserted into the database"""
        cursor = self.__get_cursor()
        cursor.execute(
            "INSERT INTO notes(title, note_source, is_public, teacher_id, category_id, "
            "note) VALUES(?, ?, ?, ?, ?, ?)",
            (title, note_source, is_public, teacher_id, category_id, note),
        )
        cursor.connection.commit()
        return cursor.lastrowid

    def get_all_notes(self, teacher_id):
        """Selects specific notes where teacher_id is connected"""
        cursor = self.__get_cursor()
        cursor.execute(
            "SELECT * FROM notes INNER JOIN categories ON notes.category_id = categories.category_id WHERE teacher_id ="
            + teacher_id
        )
        return cursor.fetchall()
    
    def get_total_entries(self, teacher_id):
        """Gets the total number of entries for a given teacher_id"""
        cursor = self.__get_cursor()
        cursor.execute(
            "SELECT COUNT(*) FROM notes WHERE teacher_id = ?",
            (teacher_id,)
        )
        result = cursor.fetchone()
        return result[0] if result is not None else 0
    
    
    def get_paginated_notes(self, teacher_id, offset, limit):
        """Selects specific notes where teacher_id is connected with pagination"""
        cursor = self.__get_cursor()
        cursor.execute(
            "SELECT * FROM notes INNER JOIN categories ON notes.category_id = categories.category_id WHERE teacher_id = ? LIMIT ? OFFSET ?",
            (teacher_id, limit, offset)
        )
        return cursor.fetchall()

    def update_note(
        self, title, note_source, is_public, teacher_id, category_id, note, note_id
    ):
        """Updates a specific note where note_id is connected to"""
        cursor = self.__get_cursor()
        cursor.execute(
            "UPDATE notes SET title=(?), note_source=(?), is_public=(?), teacher_id=(?), category_id=(?), "
            "note=(?) WHERE note_id=(?)",
            [title, note_source, is_public, teacher_id, category_id, note, note_id],
        )
        cursor.connection.commit()
        return cursor.lastrowid

    def select_note(self, note_id):
        """Selects a specific note where note_id is connected to"""
        cursor = self.__get_cursor()
        cursor.execute(
            "SELECT * FROM notes INNER JOIN categories ON notes.category_id = categories.category_id INNER JOIN "
            "teachers ON notes.teacher_id = teachers.teacher_id WHERE note_id=(?)",
            [note_id],
        )
        cursor.connection.commit()
        return cursor.fetchall()

    def delete_note(self, note_id):
        """Deletes a specific note where note_id is connected to"""
        cursor = self.__get_cursor()
        cursor.execute("DELETE FROM notes WHERE note_id=(?)", [note_id])
        cursor.connection.commit()
        return cursor.fetchall()

    def search_note(self, teacher_id, search_value, offset, limit):
        """Selects specific notes where teacher_id and search_value are related to"""
        cursor = self.__get_cursor()
        query = (
            "SELECT * FROM notes "
            "INNER JOIN categories ON notes.category_id = categories.category_id "
            "WHERE teacher_id = ? AND (title LIKE ? OR note LIKE ?) "
            "LIMIT ? OFFSET ?"
        )
        params = [teacher_id, f"%{search_value}%", f"%{search_value}%", limit, offset]
        cursor.execute(query, params)
        return cursor.fetchall()

    def filter_note_by_category(self, teacher_id, filter_value, offset, limit):
        """Selects specific notes where teacher_id and filter_value are connected to"""
        cursor = self.__get_cursor()
        query = (
            "SELECT * FROM notes "
            "INNER JOIN categories ON notes.category_id = categories.category_id "
            "WHERE teacher_id = ? AND notes.category_id = ? "
            "LIMIT ? OFFSET ?"
        )
        params = [teacher_id, filter_value, limit, offset]
        cursor.execute(query, params)
        return cursor.fetchall()

    def filter_note_by_teacher(self, offset, limit):
        """Selects all notes which are public with pagination"""
        cursor = self.__get_cursor()
        query = (
            "SELECT * FROM notes "
            "INNER JOIN categories ON notes.category_id = categories.category_id "
            "WHERE is_public = 1 "
            "LIMIT ? OFFSET ?"
        )
        params = [limit, offset]
        cursor.execute(query, params)
        
        return cursor.fetchall()
    

    
