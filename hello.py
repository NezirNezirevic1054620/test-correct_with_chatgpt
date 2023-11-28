import sqlite3


def search_note(search_value):
    database_file = "databases/testgpt.db"
    conn = sqlite3.connect(database_file)
    c = conn.cursor()
    result = c.execute("SELECT * FROM notes WHERE title LIKE (?)", [search_value])
    print(result.fetchall())

if __name__ == "__main__":
    search_note(search_value="test1234")