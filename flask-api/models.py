from main import db


class File(db.Model):
    __tablename__ = "files"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    extension = db.Column(db.String(10))
    path = db.Column(db.String(200))
    date = db.Column(db.DateTime)

    def __repr__(self):
        return "<File %r>" % (self.name)
