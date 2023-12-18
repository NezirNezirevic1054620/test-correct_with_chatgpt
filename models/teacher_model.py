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

    def delete_teacher(self, teacher_id):
        """Deletes a teacher where teacher_id is connected to teacher_id"""
        cursor = self.__get_cursor()
        cursor.execute("DELETE FROM teachers WHERE teacher_id=(?)", [teacher_id])
        cursor.connection.commit()
        return cursor.fetchall()

    def update_teacher(self, display_name, username, teacher_password, is_admin):
        """Updates teacher details where teacher_id is connected to teacher_id"""
        cursor = self.__get_cursor()
        cursor.execute(
            "UPDATE teachers SET display_name=(?), username=(?), teacher_password=(?), is_admin=(?) "
            "WHERE teacher_id=(?)",
            [display_name, username, teacher_password, is_admin],
        )
        cursor.connection.commit()
        return cursor.lastrowid

    def search_teacher(self, search_value):
        """Selects a specific teacher where display_name and username are connected to search_value"""
        cursor = self.__get_cursor()
        cursor.execute(
            "SELECT * FROM teachers WHERE display_name LIKE (?) OR username LIKE (?)",
            [f"%{search_value}%", f"%{search_value}%"],
        )
        cursor.connection.commit()
        return cursor.fetchall()
