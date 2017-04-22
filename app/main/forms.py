from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import  Required


class NameFrom(FlaskForm):
    name = StringField('What is your name?',validators=[Required()])
    submit = SubmitField('Submit')