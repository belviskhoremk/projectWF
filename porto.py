from flask import render_template
from app import app

@app.route("/porto")
def porto():
    return "<p>This is my porto</p>"
        #render_template("porto.html")