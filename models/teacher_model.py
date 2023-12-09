from sqlite3 import Error
from models.database_connector import DatabaseConnector


class TeacherModel(DatabaseConnector):
    database = DatabaseConnector()
    cursor = database.connect().cursor()

    @staticmethod
    def select_teachers():
        TeacherModel.database.connect()
        try:
            TeacherModel.cursor.execute("SELECT * FROM teachers")
            TeacherModel.cursor.connection.commit()
            teachers = TeacherModel.cursor.fetchall()
            print(teachers)
            return teachers
        except Error as error:
            print(error)

    @staticmethod
    def login(username):
        TeacherModel.database.connect()
        try:
            TeacherModel.cursor.execute("SELECT * FROM teachers WHERE username = (?)", [username])
            TeacherModel.cursor.connection.commit()
            teacher = TeacherModel.cursor.fetchall()
            print(teacher)
            return teacher
        except Error as error:
            print(error)

    @staticmethod
    def insert_teacher(display_name, username, teacher_password, is_admin):
        TeacherModel.database.connect()
        try:
            TeacherModel.cursor.execute(
                "INSERT INTO teachers (display_name, username, teacher_password, is_admin) VALUES (?, ?, ?, ?)",
                (display_name, username, teacher_password, is_admin))
            TeacherModel.cursor.connection.commit()
            result = TeacherModel.cursor.fetchall()
            print(result)
            return result
        except Error as error:
            print(error)
