from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CategoryForm(FlaskForm):
    omschrijving = StringField('omschrijving', validators=[DataRequired(), Length(min=3, max=15)])