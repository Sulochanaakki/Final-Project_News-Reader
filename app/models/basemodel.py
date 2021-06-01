
from flask_sqlalchemy import SQLAlchemy
from app.config import db

#db = SQLAlchemy()

class Base(db.Model):
    __abstract__ =True
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    date_created = db.Column(db.DateTime,default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


    def __init__(self, id):
        self.id = id

    def json(self):
        obj = {
            'id': self.id
        }
        return obj


