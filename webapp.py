from flask import Flask
from app import routes, app
from flask import render_template


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('main.html')