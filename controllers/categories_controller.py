from sqlite3 import Error
from controllers.database_connector import DatabaseConnector


class CategoriesController(DatabaseConnector):

    database = DatabaseConnector()
    cursor = database.connect().cursor()

    @staticmethod
    def select_categories():
        CategoriesController.database.connect()
        try:
            CategoriesController.cursor.execute("SELECT * FROM categories")
            CategoriesController.cursor.connection.commit()
            categories = CategoriesController.cursor.fetchall()
            return categories
        except Error as error:
            print(error)
            