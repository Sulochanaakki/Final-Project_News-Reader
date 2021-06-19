import unittest
import os
from app.config import app,db

from app.models.allnewsmodel import AllNewsModel

from os.path import abspath, dirname, join

project_dir = os.path.dirname(os.path.abspath(__file__))

'''SECRET_KEY = 'flask-session-insecure-secret-key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(_cwd, 'flask-tracking.db')
SQLALCHEMY_ECHO = True'''


class BaseConfiguration(object):
    DEBUG =False
    TESTING = False
    SECRET_KEY = 'flask-session-insecure-secret-key'

class TestConfiguration(BaseConfiguration):
    TESTING = True
    WTF_CSRF_ENABLED = False

    database_file = "sqlite:///{}".format(os.path.join(project_dir,"db/newsdatabase.sqlite"))
    SQLALCHEMY_DATABASE_URI = database_file
    # Since we want our unit tests to run quickly
    # we turn this down - the hashing is still done
    # but the time-consuming part is left out.
    HASH_ROUNDS = 1

from flask import url_for

from test_base import BaseTestCase
from models.allnewsmodel import AllNewsModel


class UserViewsTests(BaseTestCase):
    def test_allnews(self):
        AllNewsModel.create(
            source="TechCrunch",
            author="Darrell Etherington",
            title="Google Cloud teams up with SpaceX\u2019s Starlink for enterprise connectivity at network\u2019s edge",
            description="SpaceX\u2019s bourgeoning Starlink satellite-based broadband internet service just got a big boost from a significant new partner: Google Cloud. Thanks to a new partnership between the two, SpaceX will now be locating Starlink ground stations right within Google\u2019s\u2026",
            url="http://techcrunch.com/2021/05/13/google-cloud-teams-up-with-spacexs-starlink-for-enterprise-connectivity-at-networks-edge/",
            urlToImage="https://techcrunch.com/wp-content/uploads/2021/03/starlink-satellites-on-orbit.jpg?w=711",
            publishedAt="2021-05-13T13:24:58Z",
            content="SpaceX\u2019s bourgeoning Starlink satellite-based broadband internet service just got a big boost from a significant new partner: Google Cloud. Thanks to a new partnership between the two, SpaceX will no\u2026 [+1678 chars]"
        )

        response = self.client.post(url_for('allnews'),
                                    data={'source':"TechCrunch",
    'author':"Darrell Etherington",
    'title':"Google Cloud teams up with SpaceX\u2019s Starlink for enterprise connectivity at network\u2019s edge",
    'description': "SpaceX\u2019s bourgeoning Starlink satellite-based broadband internet service just got a big boost from a significant new partner: Google Cloud. Thanks to a new partnership between the two, SpaceX will now be locating Starlink ground stations right within Google\u2019s\u2026",
    'url':"http://techcrunch.com/2021/05/13/google-cloud-teams-up-with-spacexs-starlink-for-enterprise-connectivity-at-networks-edge/",
    'urlToImage':"https://techcrunch.com/wp-content/uploads/2021/03/starlink-satellites-on-orbit.jpg?w=711",
    'publishedAt': "2021-05-13T13:24:58Z",
    'content': "SpaceX\u2019s bourgeoning Starlink satellite-based broadband internet service just got a big boost from a significant new partner: Google Cloud. Thanks to a new partnership between the two, SpaceX will no\u2026 [+1678 chars]"
     })

        self.assert_redirects(response, url_for('tracking.index'))





'''def _init_database():

    data = AllNewsModel(

    source="TechCrunch",
    author="Darrell Etherington",
    title="Google Cloud teams up with SpaceX\u2019s Starlink for enterprise connectivity at network\u2019s edge",
    description= "SpaceX\u2019s bourgeoning Starlink satellite-based broadband internet service just got a big boost from a significant new partner: Google Cloud. Thanks to a new partnership between the two, SpaceX will now be locating Starlink ground stations right within Google\u2019s\u2026",
    url="http://techcrunch.com/2021/05/13/google-cloud-teams-up-with-spacexs-starlink-for-enterprise-connectivity-at-networks-edge/",
    urlToImage= "https://techcrunch.com/wp-content/uploads/2021/03/starlink-satellites-on-orbit.jpg?w=711",
    publishedAt= "2021-05-13T13:24:58Z",
    content = "SpaceX\u2019s bourgeoning Starlink satellite-based broadband internet service just got a big boost from a significant new partner: Google Cloud. Thanks to a new partnership between the two, SpaceX will no\u2026 [+1678 chars]"
     )
    db.session.add(data)
    db.session.commit(data)
    return data

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = database_file
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

        _init_database()  # init database every time

    def tearDown(self):
        db.session.remove()
        db.drop_all()



    def test_case_1(self):
        self.assertTrue(AllNewsModel.query.count() == 1)  # case 1

    def test_case_2(self):
        self.assertTrue(AllNewsModel.query.count() == 1)  # case 1

if __name__ == '__main__':
    unittest.main()'''