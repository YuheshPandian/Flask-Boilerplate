from flask import Flask

app = Flask(__name__)

from .views import app, page_not_found

app.register_error_handler(404, page_not_found)
app.config.from_pyfile("config.py")


from app import views
