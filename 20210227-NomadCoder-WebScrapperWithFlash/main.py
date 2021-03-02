from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file

app = Flask("SuperScrapper")
db = {}


@app.route("/")
def home():
    return render_template("potato.html")


@app.route("/<username>")
def potato(username):
    return f"Hello {username} how are you doing"


@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template(
        "report.html",
        searchingBy=word,
        resultsNumber=len(jobs),
        jobs=jobs
    )


@app.route("/export")
def export():
    word = request.args.get('word')
    if word:
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            return redirect("/")
        save_to_file(jobs)
        return send_file('job.csv', mimetype='application/x-csv', attachment_filename='summary_report.csv', as_attachment=True)
    else:
        return redirect("/")


app.run()
