from flask import Blueprint 

views = Blueprint('views')


@views.route('/')
def home():
    return "<h1>Test</h1"
