from sqlite3 import Error
from models.database_connector import DatabaseConnector


class CategoryModel(DatabaseConnector):
    database = DatabaseConnector()
    cursor = database.connect().cursor()

    @staticmethod
    def select_categories():
        CategoryModel.database.connect()
        try:
            CategoryModel.cursor.execute("SELECT * FROM categories")
            CategoryModel.cursor.connection.commit()
            categories = CategoryModel.cursor.fetchall()
            print(categories)
            return categories
        except Error as error:
            print(error)

    @staticmethod
    def insert_category(omschrijving):
        CategoryModel.database.connect()
        try:
            CategoryModel.cursor.execute(
                "INSERT INTO categories(omschrijving) VALUES(?)", [omschrijving])
            CategoryModel.cursor.connection.commit()
            return CategoryModel.cursor.lastrowid
        except Error as error:
            print(error)

    @staticmethod
    def delete_category(category_id):
        CategoryModel.database.connect()
        try:
            CategoryModel.cursor.execute(
                "DELETE FROM categories WHERE category_id=" + category_id)
            CategoryModel.cursor.connection.commit()
        except Error as error:
            print(error)

    @staticmethod
    def select_category(category_id):
        CategoryModel.database.connect()
        try:
            CategoryModel.cursor.execute(
                "SELECT * FROM categories WHERE category_id=" + category_id)
            CategoryModel.cursor.connection.commit()
            return CategoryModel.cursor.fetchall()
        except Error as error:
            print(error)

    @staticmethod
    def update_category(category_id, omschrijving):
        CategoryModel.database.connect()
        try:
            CategoryModel.cursor.execute("UPDATE categories SET omschrijving = '" + omschrijving + "' WHERE " +
                                                "category_id=" + category_id)
            CategoryModel.cursor.connection.commit()
            return CategoryModel.cursor.fetchone()
        except Error as error:
            print(error)

    @staticmethod
    def search_category(search_value):
        CategoryModel.database.connect()
        try:
            CategoryModel.cursor.execute(
                "SELECT * FROM categories WHERE categories.omschrijving LIKE (?)", ['%' + search_value + '%'])
            CategoryModel.cursor.connection.commit()
            category = CategoryModel.cursor.fetchall()
            print(category)
            return category
        except Error as error:
            print(error)
