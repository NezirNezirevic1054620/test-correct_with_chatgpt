import sqlite3
from pathlib import Path


class TeacherModel:
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

    def insert_teacher(self, display_name, username, teacher_password, is_admin):
        cursor = self.__get_cursor()
        cursor.execute("INSERT INTO teachers (display_name, username, teacher_password, is_admin) VALUES (?, ?, ?, ?)",
                       (display_name, username, teacher_password, is_admin))
        cursor.connection.commit()
        return cursor.lastrowid

    def get_all_teachers(self):
        cursor = self.__get_cursor()
        cursor.execute("SELECT * FROM teachers")
        return cursor.fetchall()

    def login(self, username):
        cursor = self.__get_cursor()
        cursor.execute("SELECT * FROM teachers WHERE username = (?)", [username])
        return cursor.fetchall()

# @staticmethod
# def select_teachers():
#     TeacherModel.database.connect()
#     try:
#         TeacherModel.cursor.execute("SELECT * FROM teachers")
#         TeacherModel.cursor.connection.commit()
#         teachers = TeacherModel.cursor.fetchall()
#         print(teachers)
#         return teachers
#     except Error as error:
#         print(error)
#
# @staticmethod
# def login(username):
#     TeacherModel.database.connect()
#     try:
#         TeacherModel.cursor.execute("SELECT * FROM teachers WHERE username = (?)", [username])
#         TeacherModel.cursor.connection.commit()
#         teacher = TeacherModel.cursor.fetchall()
#         print(teacher)
#         return teacher
#     except Error as error:
#         print(error)
#
# @staticmethod
# def insert_teacher(display_name, username, teacher_password, is_admin):
#     TeacherModel.database.connect()
#     try:
#         TeacherModel.cursor.execute(
#             "INSERT INTO teachers (display_name, username, teacher_password, is_admin) VALUES (?, ?, ?, ?)",
#             (display_name, username, teacher_password, is_admin))
#         TeacherModel.cursor.connection.commit()
#         result = TeacherModel.cursor.fetchall()
#         print(result)
#         return result
#     except Error as error:
#         print(error)
