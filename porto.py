from flask import Blueprint,render_template


bp =Blueprint('porto',__name__)

@bp.route("/porto")
def porto():
    return "<p>This is my porto</p>"
        #render_template("porto.html")