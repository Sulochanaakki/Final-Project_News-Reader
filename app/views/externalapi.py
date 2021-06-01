from flask import Flask

import run
from run import app
import requests
import json
@app.route('/headlines')
def headlines():

    query_params = {
        "sources": "bbc-news,the-verge",
        "sortBy": "publishedAt",
        "apiKey": "e90358389f0b41b2bf25bfc55c92f69c"
    }

    main_url = "https://newsapi.org/v2/top-headlines"
    my_headlines = requests.get(main_url, params=query_params)
    open_page = my_headlines.json()
    #return open_page

    with open('app\\db\\newsheadlines.json', 'w') as outfile:
        json.dump(open_page, outfile, indent=4)



@app.route('/allnews')
def all_news():
    #following query parameters are used
    #source,sortBy and apiKey
    query_params = {
        'q': 'big data',  # query phrase
         'pageSize': 20,  # maximum is 100
        "apiKey": "e90358389f0b41b2bf25bfc55c92f69c"
    }
    main_url = 'https://newsapi.org/v2/everything?'
    my_headlines = requests.get(main_url, params=query_params)
    open_page = my_headlines.json()
    #return open_page

    with open('app\\db\\allnews.json', 'w') as outfile:
        json.dump(open_page, outfile, indent=4)


@app.route('/sources')
def sources():
    #following query parameters are used
    #source,sortBy and apiKey
    query_params = {
        'pageSize': 20,  # maximum is 100
        "apiKey": "e90358389f0b41b2bf25bfc55c92f69c"
    }
    main_url = "https://newsapi.org/v2/sources?"
    my_headlines = requests.get(main_url, params=query_params)
    open_page = my_headlines.json()
    #return open_page


    with open('app\\db\\sources.json', 'w') as outfile:
        json.dump(open_page, outfile, indent=4)