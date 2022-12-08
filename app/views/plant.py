from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.forms.plant import PlantsForm
from app.models.plant import Plants

plant_blueprint = Blueprint("plant", __name__)

@plant_blueprint.route("/plant/register", methods=["GET", "POST"])
def register():
    form = PlantsForm(request.form)
    if form.validate_on_submit():
        plant = Plants(
            title=form.title.data,
            location=form.location.data,
        )
        plant.save()
        flash("Registration is successful", "success")
        return redirect(url_for("main.index"))
    elif form.is_submitted():
        flash("The given data was invalid.", "danger")
    return render_template("plant/register.html", form=form)