from parser import parse_log_file
from main import app, db
from models import File


@app.route("/")
def index():
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
    return "Parsing..."


@app.route("/api/rsync/logs_count")
def rsync_logs_count():
    return "12"
