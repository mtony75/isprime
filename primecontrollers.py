from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, validators

class IsPrime(FlaskForm):
    userNumber = IntegerField("Number")
    submit = SubmitField("Send")

class RangeOfPrimes(FlaskForm):
    firstNumber = IntegerField("Number1")
    secondNumber = IntegerField("Number2")
    submit = SubmitField("Send")