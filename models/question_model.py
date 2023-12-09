from sqlite3 import Error
from models.database_connector import DatabaseConnector


class QuestionModel(DatabaseConnector):
    database = DatabaseConnector()
    cursor = database.connect().cursor()

    @staticmethod
    def select_questions():
        QuestionModel.database.connect()
        try:
            QuestionModel.cursor.execute(
                "SELECT * FROM questions INNER JOIN notes ON notes.note_id = questions.note_id")
            QuestionModel.cursor.connection.commit()
            questions = QuestionModel.cursor.fetchall()
            print(questions)
            return questions
        except Error as error:
            print(error)

    @staticmethod
    def insert_question(note_id, exam_question):
        QuestionModel.database.connect()
        try:
            QuestionModel.cursor.execute(
                "INSERT INTO questions (note_id, exam_question) VALUES(?,?)", [note_id, exam_question])
            QuestionModel.cursor.connection.commit()
            return QuestionModel.cursor.lastrowid
        except Error as error:
            print(error)

    @staticmethod
    def delete_question(note_id):
        QuestionModel.database.connect()
        try:
            QuestionModel.cursor.execute(
                "DELETE FROM exam_questions WHERE note_id=" + note_id)
            QuestionModel.cursor.connection.commit()
        except Error as error:
            print(error)

    @staticmethod
    def generate_question(note_id, question):
        QuestionModel.database.connect()
        try:
            QuestionModel.cursor.execute("UPDATE questions SET exam_question = '" + question + "' WHERE " +
                                               "note_id=" + note_id)
            QuestionModel.cursor.connection.commit()
            return QuestionModel.cursor.fetchone()
        except Error as error:
            print(error)
