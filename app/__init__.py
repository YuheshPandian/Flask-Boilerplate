"""
This file initializes the app
"""

from flask import Flask


app = Flask(__name__)

app.config.from_pyfile("config.py")


def register_views():
    from app import views


register_views()
