import os


class Config():
    SECRET_KEY = os.environ.get("SECRET_KEY") or ""
    SQLALCHEMY_DATABASE_URI = "mysql://gabastil1@{SECRET_KEY}gabastil1.db.8756087.hostedresource.com/gabastil1"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
