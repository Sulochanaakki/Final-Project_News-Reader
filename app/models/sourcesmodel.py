from app.models.basemodel import Base
from sqlalchemy.orm import relationship, backref
from app.models.allnewsmodel import AllNewsModel
from app.models.headlinesmodel import HeadlineModel
from app.config import db

class SourceModel(Base):
    __tablename__ ='sources'
    __table_args__ = {'sqlite_autoincrement': True}


    headlines_id =db.Column(db.Integer,db.ForeignKey('headlines.id'))
    allnews_id = db.Column(db.Integer, db.ForeignKey('allnews.id'))
    name = db.Column(db.String(255))
    description = db.Column(db.String)
    url = db.Column(db.String)
    category = db.Column(db.String(500))
    language = db.Column(db.String(100))
    country = db.Column(db.String(100))

    headline = relationship(HeadlineModel, backref=backref("headlines", cascade="all, delete-orphan"))
    allnews = relationship(AllNewsModel, backref=backref("allnews", cascade="all, delete-orphan"))


    def __init__(self,headlines_id,allnews_id,name,description,url,category,language,country):
        self.headlines_id = headlines_id
        self.allnews_id = allnews_id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country


    def json(self):
        obj = {
            'headlines_id': self.headlines_id,
            'allnews_id': self.allnews_id,
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

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


