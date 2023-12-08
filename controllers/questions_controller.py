from sqlite3 import Error
from controllers.database_connector import DatabaseConnector


class QuestionsController(DatabaseConnector):
    database = DatabaseConnector()
    cursor = database.connect().cursor()

    @staticmethod
    def select_questions():
        QuestionsController.database.connect()
        try:
            QuestionsController.cursor.execute(
                "SELECT * FROM questions")
            QuestionsController.cursor.connection.commit()
            questions = QuestionsController.cursor.fetchall()
            print(questions)
            return questions
        except Error as error:
            print(error)

    @staticmethod
    def insert_question(note_id, exam_question):
        QuestionsController.database.connect()
        try:
            QuestionsController.cursor.execute(
                "INSERT INTO questions (note_id, exam_question) VALUES(?,?)", [note_id, exam_question])
            QuestionsController.cursor.connection.commit()
            return QuestionsController.cursor.lastrowid
        except Error as error:
            print(error)

    @staticmethod
    def delete_question(note_id):
        QuestionsController.database.connect()
        try:
            QuestionsController.cursor.execute(
                "DELETE FROM exam_questions WHERE note_id=" + note_id)
            QuestionsController.cursor.connection.commit()
        except Error as error:
            print(error)

    @staticmethod
    def generate_question(note_id, question):
        QuestionsController.database.connect()
        try:
            QuestionsController.cursor.execute("UPDATE questions SET exam_question = '" + question + "' WHERE " +
                                               "note_id=" + note_id)
            QuestionsController.cursor.connection.commit()
            return QuestionsController.cursor.fetchone()
        except Error as error:
            print(error)
