from flask import render_template, redirect, url_for, flash
from parser import parse_log_file
from main import app, db
from models import File


@app.route("/")
def index():
    return render_template("index.html", title="Log Parser")


@app.route("/rsync")
def rsync():
    logs = db.session.query(File).all()
    return render_template("rsync/logs.html", title="Rsync Logs", logs=logs)


@app.route("/rsync/parse")
def rsync_logs_parse():
    files = parse_log_file()

    for file in files:
        file = File(
            name=file["name"],
            extension=file["extension"],
            path=file["path"],
            date=file["date_time"],
        )
        db.session.add(file)

    db.session.commit()
    flash("Rsync log successfully parsed")
    return redirect(url_for("rsync"))


@app.route("/prometheus")
def prometheus():
    return redirect("http://localhost:9090")


@app.route("/grafana")
def grafana():
    return redirect("http://localhost:3000")


@app.route("/api/rsync/logs_count")
def rsync_logs_count():
    count = db.session.query(File).count()
    return {"NumLogs": count}
