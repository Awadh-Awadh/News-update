import urllib.request,json
from .models import Source

api_key = None
base_url = None
article_url = None

def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_url = app.config['NEWS_ARTICLE_URL']

def get_sources():
    with urllib.request.urlopen(base_url) as url:
        get_url_data = url.read()
        get_source_response = json.loads(get_url_data)

        source_results = None
        if get_source_response['sources']:
            source_list = get_source_response['sources']
            source_results = process_result(source_list)

        return source_results

def process_result(source_list):
    '''Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain movie details

    Returns :
        source_results: A list of movie objects
    '''
    source_results = []

    for item in source_list:
        id = item.get('id')
        name = item.get('name')
        source_object = Source(id, name)
        source_results.append(source_object)

        return source_results
