from sqlalchemy.orm import relationship
from app.config import db
class HeadlineModel(db.Model):
    __tablename__ ='headlines'
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    source = db.Column(db.String(200))
    author = db.Column(db.String(500))
    title = db.Column(db.String)
    description = db.Column(db.String)
    url = db.Column(db.String)
    urlToImage = db.Column(db.String)
    publishedAt = db.Column(db.String)
    content = db.Column(db.String)

    allnews = relationship('AllNewsModel', secondary='sources')


    def __init__(self,id,source,author,title,description,url,urlToImage,publishedAt,content):
        id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)


    def json(self):
        obj = {
            'id': self.id,
            'source': self.source,
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'url' : self.url,
            'urlToImage':  self.urlToImage,
            'publishedAt': self.publishedAt,
            'content': self.content
        }
        return obj


    @classmethod
    def find_by_id(cls,_id)->"HeadlineModel":
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