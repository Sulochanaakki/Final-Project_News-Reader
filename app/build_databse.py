from externalapi import all_news_feed,headlines_feed,sources_feed
from models.allnewsmodel import AllNewsModel
from models.headlinesmodel import HeadlineModel
from models.sourcesmodel import SourceModel
from config import db
allnews_data = all_news_feed()
print(allnews_data)
for row in allnews_data['articles']:
    db_record = AllNewsModel(
        source=str(row['source']['name']),
        author=row['author'],
        title=row['title'],
        description=row['description'],
        url=row['url'],
        urlToImage=row['urlToImage'],
        publishedAt=row['publishedAt'],
        content=row['content']
    )
    db.session.add(db_record)
db.session.commit()
print("db added")

headlines_data = headlines_feed()
print(headlines_data)
for row in headlines_data['articles']:
    db_record =HeadlineModel (
        source=str(row['source']['name']),
        author=row['author'],
        title=row['title'],
        description=row['description'],
        url=row['url'],
        urlToImage=row['urlToImage'],
        publishedAt=row['publishedAt'],
        content=row['content']
    )
    db.session.add(db_record)
db.session.commit()
print("db added")

sources_data = sources_feed()
print(sources_data)
for row in sources_data['sources']:
    db_record =SourceModel (
        name=row['name'],
        description=row['description'],
        url=row['url'],
        category=row['category'],
        language=row['language'],
        country=row['country']
    )
    db.session.add(db_record)
db.session.commit()
print("db added")