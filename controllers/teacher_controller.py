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
