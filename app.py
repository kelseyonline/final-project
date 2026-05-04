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
def home():
    return render_template("index.html")

@app.route("/track")
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

@app.route('/stats', methods=["GET"])
def stats():
    max_weight = 0
    # This one is a dictionary because it is machine + number
    machine_counts = {}
    date_counts = {}

    with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            # This part deals with max weight
            if len(row) > 3:  # making sure weight column exists
                try:
                    weight = float(row[3])  # convert string to a number
                    if weight > max_weight:
                        max_weight = weight
                except ValueError:
                    continue  # skip bad data (like empty strings)
            
            # This part deals with the most common machine
            if len(row) > 2:
                machine = row[2].strip()

                if machine in machine_counts:
                    machine_counts[machine] += 1
                else:
                    machine_counts[machine] = 1

            # This part calculates the most common day 
            if len(row) > 0 and row[0].strip():
                day = row[0].strip()
                date_counts[day] = date_counts.get(day, 0) + 1

    most_used_machine = None
    if machine_counts: 
        most_used_machine = max(machine_counts, key=machine_counts.get)

    most_common_day = None
    if date_counts: 
        most_common_day = max(date_counts, key=date_counts.get)
        
    return render_template('stats.html', max_weight=max_weight, most_used_machine=most_used_machine, most_common_day=most_common_day)

if __name__ == "__main__":
    app.run(debug=True, port=5050)