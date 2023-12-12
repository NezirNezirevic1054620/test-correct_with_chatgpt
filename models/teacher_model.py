"""Teacher Model with all its sql queries"""
import sqlite3
from pathlib import Path


class TeacherModel:
    """TeacherModel class with all its methods"""

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

    def insert_teacher(self, display_name, username, teacher_password, is_admin):
        """Teacher gets inserted into the database"""
        cursor = self.__get_cursor()
        cursor.execute(
            "INSERT INTO teachers (display_name, username, teacher_password, is_admin) VALUES (?, ?, ?, ?)",
            (display_name, username, teacher_password, is_admin),
        )
        cursor.connection.commit()
        return cursor.lastrowid

    def get_all_teachers(self):
        """Selects all teachers from the database"""
        cursor = self.__get_cursor()
        cursor.execute("SELECT * FROM teachers")
        return cursor.fetchall()

    def login(self, username):
        """Selects a specific row from the database if the username is correct"""
        cursor = self.__get_cursor()
        cursor.execute("SELECT * FROM teachers WHERE username = (?)", [username])
        return cursor.fetchall()
