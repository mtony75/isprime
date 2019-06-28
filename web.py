from flask import Flask
from flask import render_template
# from app import app

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('main.html')

if __name__ == '__main__':
    app.run()