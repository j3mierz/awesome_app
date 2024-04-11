from flask import Flask
from datetime import datetime
from random import randint
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "użytkowniku user"


@app.route("/hello/<username>")
def name(username):
    return username


@app.route("/time")
def get_time():
    return str(datetime.time(datetime.now()))


@app.route("/date")
def get_date():
    return str(datetime.date(datetime.now()))


@app.route("/licz/<int:a>/<int:b>")
def count(a, b):
    return str(a + b)


@app.route("/losuj")
def dice():
    return f'{randint(0, 9)}, {randint(0, 9)}, {randint(0, 9)}'

@app.route("/lotek")
def lotto():
    result = []
    while len(result) <= 6:
        a = randint(0, 50)
        if a not in result:
            result.append(str(a))
    return ", ".join(result)

