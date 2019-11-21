from flask import render_template

from app import app
from service.services import recipe_service


@app.route('/index', methods=['GET'])
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'name': 'Kirill',
            'id': 1
        },
        {
            'name': 'Lolloo',
            'id': 2
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'


# @app.route('/kirill', methods=['GET', 'POST' ...])
@app.route('/kirill', methods=['GET'])
def get_recipe():
    recipe_service.get_recipe(['onion', 'garlic'])
    return 'Kirill'

