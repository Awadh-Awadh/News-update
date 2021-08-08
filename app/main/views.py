from flask import render_template, request, url_for, redirect
from . import main
from ..requests import get_sources
# from ..models import Source


@main.route('/')
def index():
    general = get_sources()
    

    

    return render_template('index.html', message = general)