from flask import Flask

app = Flask(__name__)

from .views import app, page_not_found


app.config.from_pyfile("config.py")
