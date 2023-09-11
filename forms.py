from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class GetEquationForm(FlaskForm):
    usereq=StringField("Type your guess here:",validators=[DataRequired()])
    submit=SubmitField("Enter Equation")