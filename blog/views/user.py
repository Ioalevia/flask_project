from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required

from werkzeug.exceptions import NotFound

from blog.models import UserModel
from blog.views.auth import login_manager

users_app = Blueprint("users_app", __name__)


@users_app.route("/", endpoint="list")
def users_list():
    users = UserModel.query.all()
    return render_template("user/list.html", users=users)


@users_app.route("/<int:user_index>/", endpoint="detail")
@login_required
def user_detail(user_index: int):
    user = UserModel.query.filter_by(id=user_index).one_or_none()
    if user is None:
        raise NotFound(f"User #{user_index} no found.")
    return render_template("user/detail.html", user=user)

