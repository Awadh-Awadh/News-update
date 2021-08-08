from flask import render_template, request, url_for, redirect
from . import main
# # from ..requests import get_news
# from ..models import Source


@main.route('/')
def index():
    message  = "Helo world"

    return render_template('index.html', message = message)