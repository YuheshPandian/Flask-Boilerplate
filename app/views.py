from flask import render_template, url_for
from app import app
from logging import FileHandler, WARNING

app.config.from_pyfile("config.py")


if not app.debug:
    file_handler = FileHandler("errolog.txt")
    file_handler.setLevel(WARNING)

    app.logger.addHandler(file_handler)


@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template("index.html")


# from flask import abort


# @app.route("/500")
# def error500():
#     return abort(500)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
