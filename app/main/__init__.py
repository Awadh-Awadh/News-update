from flask import Blueprint
from . import error, views

main = Blueprint('main', __name__)