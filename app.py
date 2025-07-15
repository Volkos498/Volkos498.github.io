from flask import Flask,render_template
import sqlite3
from db_downloaders import *
from db import get_user_all

def get_db():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)
@app.route('/')
def hi():
    return render_template('main.html')
@app.route("/test")
def test():
    users = get_user_all()
    return render_template("test.html", users = users)
@app.route('/X_a')
def X_A():
    return render_template('Iks_apocalipcice.html')
@app.route('/X')
def gi():
    count = counter()
    return render_template('X.html', count=count)
@app.route('/band')
def band_i():
    return render_template('band.html')
@app.route('/O')
def onas():
    return render_template('O_nas.html')
@app.route('/N')
def novosti():
    return render_template('Novosti.html')
if __name__ == "__main__":
    app.run(debug=True)
