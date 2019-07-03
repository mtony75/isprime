from flask import Flask, render_template, flash, request
from isprime import *
from primecontrollers import IsPrime

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('main.html')




@app.route('/isprime', methods=['GET', 'POST'])
def isprime():
    form = IsPrime()
    title = "Is Prime"
#    uNumber = form.userNumber
#    print("***************************************************")
#    print(f"Mark the number is {form.userNumber} *************")
#    print("***************************************************")
#    uNumber = request.form["userNumber"]
    if form.is_submitted():
        if form.validate():
            if isPrime(form.userNumber.data):
                theMessage = "The Number is Prime"
            else:
                theMessage = "The number is not Prime"
            return render_template('isprime.html', form=form, theMessage=theMessage, title=title)
        else:
            theMessage = "The input was not a number. Please try again."
            return render_template('isprime.html', form=form, theMessage=theMessage, title=title)
    else:
        return render_template('isprime.html', form=form, title=title)


if __name__ == '__main__':
    app.secret_key = 'This is the secret key'
    app.run(debug=True)
