from flask import render_template, url_for
from app import app
from logging import FileHandler, WARNING

if app.debug:
    file_handler = FileHandler("errolog.txt")
    file_handler.setLevel(WARNING)

    app.logger.addHandler(file_handler)



@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/r")
def layout():
    return render_template("layout.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404