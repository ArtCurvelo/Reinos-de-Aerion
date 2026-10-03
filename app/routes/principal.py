from flask import Blueprint, render_template


principal = Blueprint("principal", __name__)


@principal.route("/")
def index():
    return render_template("index.html")