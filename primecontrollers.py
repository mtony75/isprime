from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, validators

class IsPrime(FlaskForm):
    userNumber = IntegerField("Number")
    submit = SubmitField("Send")