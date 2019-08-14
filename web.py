from flask import Flask, render_template, flash, request
from isprime import *
from primecontrollers import IsPrime, RangeOfPrimes, NextHundred

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('main.html')

@app.route('/nexthundred', methods=['GET', 'POST'])
def nexthundred():
    form = NextHundred()
    title = "Next Hundred"
    nextHundredList = []
    if form.is_submitted():
        if form.validate():
            
            nextHundredList = nextHundredPrimes(form.userNumber.data)
        return render_template('nexthundred.html', form=form, title=title, nextHundredList=nextHundredList)
    else:
        theMessage = "The number is not valid"
    return render_template('nexthundred.html', form=form, theMessage=theMessage, title=title)


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

@app.route('/rangeofprimes', methods=['GET', 'POST'])
def rangeofprimes():
    form = RangeOfPrimes()
    title = "Range Of Primes"
    if form.is_submitted():
        if form.validate():
            primeList = []
            if form.firstNumber.data < form.secondNumber.data:
                primeList = rangeOfPrime(form.firstNumber.data, form.secondNumber.data)
            else:
                primeList = rangeOfPrime(form.secondNumber.data, form.firstNumber.data)
            return render_template('rangeofprimes.html', form=form, primeList=primeList, title="Range Of Primes")
        else:
            theMessage = "Input given not a number. Please try again."
            return render_template('rangeofprimes.html', form=form, title="Range Of Primes", theMessage=theMessage)
    else:
        return render_template('rangeofprimes.html', form=form, title="Range Of Primes")            

if __name__ == '__main__':
    app.secret_key = 'This is the secret key'
    app.run(debug=True)
