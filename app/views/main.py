from flask import render_template, Blueprint
from app.models import Plants

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
def index():
    return render_template("index.html")

@main_blueprint.route("/about")
def about():
    return render_template("about.html")

@main_blueprint.route("/plant")
def plant():
    all_plants = Plants.query.all()
    return render_template("plant/profile.html", all_plants=all_plants)

