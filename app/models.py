from datetime import datetime
from app import db


class Vocabulary(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(64), index=True)
    word = db.Column(db.String(64), index=True, unique=True)
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
