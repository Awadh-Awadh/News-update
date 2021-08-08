import os

class config:
    NEWS_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(config):
    pass



class DevConfig(config):

    DEBUG = True


config_options = {
  'development': DevConfig,
  'production':  ProdConfig
}