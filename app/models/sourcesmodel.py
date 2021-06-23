import json
from externalapi import sources_feed
from sqlalchemy.orm import relationship, backref
from app.config import db


class SourceModel(db.Model):
    __tablename__ ='sources'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
   # headlines_id =db.Column(db.Integer, db.ForeignKey('headlines.headline_id'))
    #allnews_id = db.Column(db.Integer, db.ForeignKey('allnews.allnews_id'))
    name = db.Column(db.String(255))
    description = db.Column(db.String)
    url = db.Column(db.String)
    category = db.Column(db.String(500))
    language = db.Column(db.String(100))
    country = db.Column(db.String(100))

    #headline = relationship(HeadlineModel, backref=backref("headlines", cascade="all, delete-orphan"))
    #allnews = relationship(AllNewsModel, backref=backref("allnews", cascade="all, delete-orphan"))


    def __init__(self,name,description,url,category,language,country):
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country


    def json(self):
        obj = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'url': self.url,
            'category': self.category,
            'language': self.language,
            'country': self.country
        }
        return obj





    @classmethod
    def find_by_id(cls, _id) -> "SourceModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls):
        query_all = cls.query.all()
        result = []
        for one_element in query_all:
            result.append(one_element.json())
        return result


    @classmethod
    def find_by_country(cls, country) -> "SourceModel":
        query = cls.query.filter_by(country=country).all()
        result = []
        for query_data in query:
            result.append(query_data)
            json_data = json.dumps(result)
        return ('title:', json_data)



    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()




