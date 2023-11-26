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
            print(categories)
            return categories
        except Error as error:
            print(error)

    @staticmethod
    def insert_category(omschrijving):
        CategoriesController.database.connect()
        try:
            CategoriesController.cursor.execute("INSERT INTO categories(omschrijving) VALUES(?)", [omschrijving])
            CategoriesController.cursor.connection.commit()
            return CategoriesController.cursor.lastrowid
        except Error as error:
            print(error)

    @staticmethod
    def delete_category(category_id):
        CategoriesController.database.connect()
        try:
            CategoriesController.cursor.execute("DELETE FROM categories WHERE category_id=" + category_id)
            CategoriesController.cursor.connection.commit()
        except Error as error:
            print(error)

    @staticmethod
    def select_category(category_id):
        CategoriesController.database.connect()
        try:
            CategoriesController.cursor.execute("SELECT * FROM categories WHERE category_id=" + category_id)
            CategoriesController.cursor.connection.commit()
            return CategoriesController.cursor.fetchall()
        except Error as error:
            print(error)

    @staticmethod
    def update_category(category_id, omschrijving):
        CategoriesController.database.connect()
        try:
            CategoriesController.cursor.execute("UPDATE categories SET omschrijving = '" + omschrijving + "' WHERE " +
                                                "category_id=" + category_id)
            CategoriesController.cursor.connection.commit()
            return CategoriesController.cursor.fetchone()
        except Error as error:
            print(error)
