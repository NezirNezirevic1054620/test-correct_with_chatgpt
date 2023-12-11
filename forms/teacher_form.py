from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length


class TeacherForm(FlaskForm):
    display_name = StringField(
        "display_name", validators=[DataRequired(), Length(min=2, max=50)]
    )
    username = StringField(
        "username", validators=[DataRequired(), Length(min=8, max=20)]
    )
    teacher_password = StringField(
        "teacher_password", validators=[DataRequired(), Length(min=8, max=100)]
    )
    is_admin = IntegerField("is_admin")
