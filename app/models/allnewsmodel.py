import json
#from app.externalapi import all_news_feed
from sqlalchemy.orm import relationship
from app.config import db
from models.headlinesmodel import HeadlineModel
class AllNewsModel(db.Model):
    __tablename__ ='allnews'
    __table_args__ = {'extend_existing': True}
    #__table_args__ = {'sqlite_autoincrement': True}



    allnews_id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    source = db.Column(db.String(500), nullable=False)
    author = db.Column(db.String(500), nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    url = db.Column(db.String)
    urlToImage = db.Column(db.String)
    publishedAt = db.Column(db.String)
    content = db.Column(db.String)


    #headline = relationship('HeadlineModel',secondary = 'sources',backref='AllNewsModel')


    def __init__(self,source,author,title,description,url,urlToImage,publishedAt,content):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content





    def __repr__(self):
        return 'HeadlineModel(source=%s, author=%s, title=%s, \
                description=%s, url=%s, urlToImage=%s,publishedAt=%s,content =%s)' % \
               ( self.name, self.author, self.title, self.description, self.url,
                self.urlToImage, self.publishedAt, self.content)


    def json(self):

        ''' #Getting all news with headlines
        allnews_headline_list = []
        allnews_headlines = AllNewsWithHeadlinesModel.query.filter_by(allnews_id=self.allnews_id)
        for allnewsheadline in allnews_headlines:
            headlines = HeadlineModel.query.filter_by(headline_id=allnewsheadline.headline_id)
            for headline in headlines:
                allnews_headline_list.append(headline.title)'''


        obj = {
            'id' : self.allnews_id,
            'source': self.source,
            'author' : self.author,
             'title' : self.title,
             'description' : self.description,
             'url' : self.url,
             'urlToImage':  self.urlToImage,
              'publishedAt': self.publishedAt,
            'content': self.content,
           # 'headline': allnews_headline_list
        }
        return obj

    @classmethod
    def find_by_id(cls, _id) -> "AllNewsModel":
        return cls.query.filter_by(allnews_id=_id).first()

    @classmethod
    def find_by_title(cls):
        query = cls.query.order_by(AllNewsModel.title).all()
        result = []
        for query_data in query:
            result.append(query_data.title)
            json_data = json.dumps(result)
        return json_data

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




