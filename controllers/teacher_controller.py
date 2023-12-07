from sqlite3 import Error
from controllers.database_connector import DatabaseConnector


class TeacherController(DatabaseConnector):
    database = DatabaseConnector()
    cursor = database.connect().cursor()

    @staticmethod
    def select_teachers():
        TeacherController.database.connect()
        try:
            TeacherController.cursor.execute("SELECT * FROM teachers")
            TeacherController.cursor.connection.commit()
            teachers = TeacherController.cursor.fetchall()
            print(teachers)
            return teachers
        except Error as error:
            print(error)

    @staticmethod
    def login(username, password):
        TeacherController.database.connect()
        try:
            TeacherController.cursor.execute("SELECT * FROM teachers WHERE username = (?) AND teacher_password = (?)", [username, password])
            TeacherController.cursor.connection.commit()
            teacher = TeacherController.cursor.fetchall()
            print(teacher)
            return teacher
        except Error as error:
            print(error)

    @staticmethod
    def insert_teacher(display_name, username, teacher_password, is_admin):
        TeacherController.database.connect()
        try:
            TeacherController.cursor.execute("INSERT INTO teachers (display_name, username, teacher_password, is_admin) VALUES (?, ?, ?, ?)", (display_name, username, teacher_password, is_admin))
            TeacherController.cursor.connection.commit()
            result = TeacherController.cursor.fetchall()
            print(result)
            return result
        except Error as error:
            print(error)