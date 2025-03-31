"""
This python file holds all the routes of the website.
And also handles logging and error pages management
"""

from logging import FileHandler, WARNING
from flask import render_template

from app import app


if not app.debug:
    file_handler = FileHandler("errolog.txt")
    file_handler.setLevel(WARNING)

    app.logger.addHandler(file_handler)


@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    """
    returns the homepage of the site
    """
    return render_template("index.html")


# from flask import abort


# @app.route("/403")
# def error403():
#     return abort(403)

# @app.route("/500")
# def error500():
#     return abort(500)


@app.errorhandler(403)
def forbidden(_):
    """
    returns the 403 errorpage of the site
    """
    return render_template("403.html"), 403


# 404 Error page
@app.errorhandler(404)
def page_not_found(_):
    """
    returns the 404 errorpage of the site
    """
    return render_template("404.html"), 404


# 500 error page
@app.errorhandler(500)
def internal_server_error(_):
    """
    returns the 500 errorpage of the site
    """
    return render_template("500.html"), 500
