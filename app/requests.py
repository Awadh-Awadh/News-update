import requests as rq
from models import Source

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
        sources_object = None
        if source_list:
            id = source_list.get('id')
            name = source_list.get('name')
            sources_object = Source(id, name)

        return sources_object

