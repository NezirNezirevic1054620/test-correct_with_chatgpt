from models.question_model import QuestionModel

DATABASE_FILE = "/Users/nezirnezirevic/Desktop/wp2-2023-mvc-1e5-nlbl/databases/testgpt.db"


def test_get_all_questions():
    question = None
    mydict = {}
    question_model = QuestionModel(DATABASE_FILE)
    questions = question_model.get_all_questions()
    for question in questions:
        mydict = {
            "questions_id": question[0],
            'note_id': question[1],
            'exam_question': question[2],
            'date_created': question[3]
        }
    assert dict(question) == mydict
