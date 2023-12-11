import sqlite3
from pathlib import Path


class QuestionModel:
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

    def get_all_questions(self):
        cursor = self.__get_cursor()
        cursor.execute(
            "SELECT * FROM questions INNER JOIN notes ON notes.note_id = questions.note_id"
        )
        return cursor.fetchall()

    def insert_question(self, note_id, exam_question):
        cursor = self.__get_cursor()
        cursor.execute(
            "INSERT INTO questions (note_id, exam_question) VALUES(?,?)",
            [note_id, exam_question],
        )
        cursor.connection.commit()
        return cursor.lastrowid
