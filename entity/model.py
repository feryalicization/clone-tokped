from . import db
from datetime import datetime



class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.DateTime)
    updated_date = db.Column(db.DateTime)
    deleted_date = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    updated_by = db.Column(db.Integer)
    username = db.Column(db.String(225))
    email = db.Column(db.String(225), unique=True)
    notlp = db.Column(db.String(225))
    password = db.Column(db.String(225))
    otp = db.Column(db.String(225))