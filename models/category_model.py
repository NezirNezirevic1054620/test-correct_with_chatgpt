""" Category Model with all its SQL queries """
import sqlite3
from pathlib import Path


class CategoryModel:
    """CategoryModel class with all its methods"""

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

    def insert_category(self, omschrijving):
        """Category row gets inserted in the database"""
        cursor = self.__get_cursor()
        cursor.execute("INSERT INTO categories(omschrijving) VALUES(?)", [omschrijving])
        cursor.connection.commit()
        return cursor.lastrowid

    def get_all_categories(self):
        """Selects all categories from the database and returns them"""
        cursor = self.__get_cursor()
        cursor.execute("SELECT * FROM categories")
        return cursor.fetchall()

    def update_category(self, omschrijving, category_id):
        """Updates a specific category row connected to the category_id"""
        cursor = self.__get_cursor()
        cursor.execute(
            "UPDATE categories SET omschrijving = (?) WHERE category_id = (?)",
            [omschrijving, category_id],
        )
        cursor.connection.commit()
        return cursor.lastrowid

    def select_category(self, category_id):
        """Selects a specific row from the database connected to the category_id"""
        cursor = self.__get_cursor()
        cursor.execute("SELECT * FROM categories WHERE category_id = (?)", [category_id])
        cursor.connection.commit()
        return cursor.fetchall()

    def delete_category(self, category_id):
        """Deletes a specific row from the database connected to the category_id"""
        cursor = self.__get_cursor()
        cursor.execute("DELETE FROM categories WHERE category_id = (?)", [category_id])
        cursor.connection.commit()
        return cursor.lastrowid

    def search_categories(self, search_value):
        """Selects specific row/rows where search_value is connected to"""
        cursor = self.__get_cursor()
        cursor.execute(
            "SELECT * FROM categories WHERE categories.omschrijving LIKE (?)",
            ["%" + search_value + "%"],
        )
        return cursor.fetchall()
