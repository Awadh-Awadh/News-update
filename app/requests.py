import requests as rq


api_key = None
base_url = None
article_url = None

def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_url = app.config['NEWS_ARTICLE_URL']

def get_sources(category):
    with rq.get(base_url.format(category,api_key)) as data:
        data = data.json()
        source_list = data.get('sources')
        return source_list

