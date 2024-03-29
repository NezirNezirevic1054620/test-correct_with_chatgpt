"""Question Model with all its SQL queries"""
import sqlite3
from pathlib import Path


class QuestionModel:
    """QuestionModel class with all its methods"""

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

    def get_all_questions(self):
        """Selects all the questions connected to the note_id from the database"""
        cursor = self.__get_cursor()
        cursor.execute(
            "SELECT * FROM questions INNER JOIN notes ON notes.note_id = questions.note_id INNER JOIN categories ON "
            "categories.category_id = notes.category_id"
        )
        return cursor.fetchall()

    def insert_question(self, note_id, exam_question):
        """Inserts a question row into the database"""
        cursor = self.__get_cursor()
        cursor.execute(
            "INSERT INTO questions (note_id, exam_question) VALUES(?,?)",
            [note_id, exam_question],
        )
        cursor.connection.commit()
        return cursor.lastrowid

    def select_question_by_note(self, note_id):
        """Selects a question connected to the note_id"""
        cursor = self.__get_cursor()
        cursor.execute(
            "SELECT * FROM questions INNER JOIN notes ON notes.note_id = questions.note_id INNER JOIN teachers ON teachers.teacher_id = notes.teacher_id WHERE notes.note_id = (?)",
            [note_id],
        )
        return cursor.fetchall()

    def delete_question(self, questions_id):
        """Deletes a specific question"""
        cursor = self.__get_cursor()
        cursor.execute("DELETE FROM questions WHERE questions_id=(?)", [questions_id])
        cursor.connection.commit()
        return cursor.fetchall()

    def search_question(self, search_value):
        """Searches for a specific question if the note or the exam question aligns
        with the search value"""
        cursor = self.__get_cursor()
        cursor.execute(
            "SELECT * FROM questions INNER JOIN notes ON notes.note_id = questions.note_id WHERE note LIKE (?) OR exam_question LIKE (?)",
            [f"%{search_value}%", f"%{search_value}%"],
        )
        cursor.connection.commit()
        return cursor.fetchall()

    def filter_questions_by_category(self, filter_value):
        """Filters the notes so that it only shows notes connected to the category_id"""
        cursor = self.__get_cursor()
        cursor.execute(
            "SELECT * FROM questions INNER JOIN notes ON notes.note_id = questions.note_id INNER JOIN categories ON "
            "categories.category_id = notes.category_id WHERE notes.category_id = (?)",
            [filter_value],
        )
        cursor.connection.commit()
        return cursor.fetchall()
