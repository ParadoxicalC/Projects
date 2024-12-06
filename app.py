from flask import Flask, render_template, url_for, request, redirect
from cs50 import SQL
from datetime import datetime
import csv
import random

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/quote', methods=['GET'])
def quote():
    with open("quotes.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for i in range(1, (random.randint(1, 1666))):
            row = next(reader)
    return render_template("quote.html", quote=row[1], author=row[0])

if __name__ == "__main__":
    app.run(debug=True)

