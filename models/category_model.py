import sqlite3
from pathlib import Path


class CategoryModel:

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

    def insert_category(self, omschrijving):
        cursor = self.__get_cursor()
        cursor.execute("INSERT INTO categories(omschrijving) VALUES(?)", [omschrijving])
        cursor.connection.commit()
        return cursor.lastrowid

    def get_all_categories(self):
        cursor = self.__get_cursor()
        cursor.execute("SELECT * FROM categories")
        return cursor.fetchall()

    def update_category(self, omschrijving, category_id):
        cursor = self.__get_cursor()
        cursor.execute("UPDATE categories SET omschrijving = (?) WHERE category_id = (?)", [omschrijving, category_id])
        cursor.connection.commit()
        return cursor.lastrowid

    def select_category(self, category_id):
        cursor = self.__get_cursor()
        cursor.execute(
            "SELECT * FROM categories WHERE category_id = (?)", [category_id])
        cursor.connection.commit()
        return cursor.fetchall()

    def delete_category(self, category_id):
        cursor = self.__get_cursor()
        cursor.execute("DELETE FROM categories WHERE category_id = (?)", [category_id])
        cursor.connection.commit()
        return cursor.lastrowid

    def search_categories(self, search_value):
        cursor = self.__get_cursor()
        cursor.execute("SELECT * FROM categories WHERE categories.omschrijving LIKE (?)", ['%' + search_value + '%'])
        return cursor.fetchall()
