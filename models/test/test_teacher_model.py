"""Tests for the TeacherModel"""
from models.teacher_model import TeacherModel

DATABASE_FILE = (
    "/Users/nezirnezirevic/Desktop/wp2-2023-mvc-1e5-nlbl/databases/testgpt.db"
)


def test_get_all_teachers():
    """Method checks if the output is a dictionary"""
    teacher = None
    mydict = {}
    teacher_model = TeacherModel(DATABASE_FILE)
    teachers = teacher_model.get_all_teachers()
    for teacher in teachers:
        mydict = {
            "teacher_id": teacher[0],
            "display_name": teacher[1],
            "username": teacher[2],
            "teacher_password": teacher[3],
            "date_created": teacher[4],
            "is_admin": teacher[5],
        }
    assert dict(teacher) == mydict
