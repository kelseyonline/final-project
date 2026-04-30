# This is going to be the backend 
# I'll use this to update the CSV/table using form submissions
# I did have to have ChatGPT help me with this 
# but I read through and gained understanding before using

from flask import Flask, render_template, request, redirect
from datetime import date as today_date
import csv

app = Flask(__name__)

CSV_FILE = "data.csv"

@app.route("/")
def form():
    return render_template("track.html")

@app.route("/submit", methods=["POST"])
def submit():
    date = today_date.today()
    muscle_group = request.form["muscle-group-select"]
    machine = request.form["machine-select"]
    weight = request.form["weight"]
    reps = request.form["reps"]

    with open(CSV_FILE, "a", newline="") as file: 
        writer = csv.writer(file)
        writer.writerow([date, muscle_group, machine, weight, reps])

    return redirect("/history")

@app.route("/history")
def history():
    data = []
    with open(CSV_FILE, "r") as file: 
        reader = csv.reader(file)
        data = list(reader)

    return render_template("history.html", data=data)

if __name__ == "__main__":
    app.run(debug=True, port=5050)