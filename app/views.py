"""
This python file holds all the routes of the website.
And also handles logging and error pages management
"""

from flask import render_template, url_for
from logging import FileHandler, WARNING

from app import app


app.config.from_pyfile("config.py")


if not app.debug:
    file_handler = FileHandler("errolog.txt")
    file_handler.setLevel(WARNING)

    app.logger.addHandler(file_handler)


# Home Page for the boilerplate
@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template("index.html")


# from flask import abort


# @app.route("/500")
# def error500():
#     return abort(500)


# 404 Error page
@app.errorhandler(404)
def page_not_found():
    return render_template("404.html"), 404


# 500 error page
@app.errorhandler(500)
def internal_server_error():
    return render_template("500.html"), 500
