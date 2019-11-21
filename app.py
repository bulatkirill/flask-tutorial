from flask import Flask, render_template

app = Flask(__name__)

from routes import routes
from routes import error_routes
