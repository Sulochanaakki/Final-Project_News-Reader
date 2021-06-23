
import requests

def headlines_feed():

    query_params = {
        "sources": "bbc-news,the-verge",
        "apiKey": "e90358389f0b41b2bf25bfc55c92f69c"
    }

    main_url = "https://newsapi.org/v2/top-headlines"
    my_headlines = requests.get(main_url, params=query_params)
    open_page = my_headlines.json()
    print(open_page)
    return open_page

#@app.route('/allnews')
def all_news_feed():

    query_params = {
        'q': 'big data',  # query phrase
         'pageSize': 20,  # maximum is 100
        "apiKey": "e90358389f0b41b2bf25bfc55c92f69c"
    }
    main_url = 'https://newsapi.org/v2/everything?'
    my_headlines = requests.get(main_url, params=query_params)
    print(my_headlines.url)
    open_page = my_headlines.json()
    return open_page

def sources_feed():
    query_params = {
        'pageSize': 20,  # maximum is 100
        "apiKey": "APIKEY"
    }
    main_url = "https://newsapi.org/v2/sources?"
    r= requests.get(main_url, params=query_params)
    print(r)
    open_page = r.json()
    return open_page



if __name__ == "__main__":
    #print newstextrequest('abc-news-au','top')

    print(sources_feed())
    print(headlines_feed())
    print(all_news_feed())
   # insert_feed('allnews', all_news_feed())