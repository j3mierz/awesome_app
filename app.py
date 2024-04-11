from flask import Flask, render_template, request
from datetime import datetime
from random import randint

app = Flask(__name__)


@app.route("/welcome")
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


@app.route("/kontakt", methods=['GET', 'POST'])
def formularz():
    if request.method == 'POST':
        first_name_1 = request.form.get('firstname')
        return render_template("confirmation.html", first_name=first_name_1)
    return render_template("form.html")


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
    return "-".join(result)


operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}


@app.route("/kalkulator", methods=['GET', 'POST'])
def kalkulator():
    result = ''
    if request.method == 'POST':
        operation = request.form.get('operation')
        try:
            d1 = float(request.form.get('digit_1'))
            d2 = float(request.form.get('digit_2'))
        except ValueError:
            return render_template("calculator_form.html", message="podaj poprawne liczby")

        result = operations.get(operation)(d1, d2)

    return render_template("calculator_form.html", result=result)

@app.route("/method", methods=['GET', 'POST'])
def type_of_comm():
    if request.method == 'POST':
        return str('ty Post')
    return str('ty GET')
