"""
This file initializes the app
"""

from flask import Flask
from app import views

app = Flask(__name__)

app.config.from_pyfile("config.py")
