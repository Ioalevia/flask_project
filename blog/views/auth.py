from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_user,
    logout_user,
    login_required,
)

from blog.models.user import UserModel

auth_app = Blueprint("auth_app", __name__)

login_manager = LoginManager()
login_manager.login_view = "auth_app.login"


@login_manager.user_loader
def load_user(user_id):
    return UserModel.query.filter_by(id=user_id).one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth_app.login"))


@auth_app.route("/login/", methods=["GET", "POST"], endpoint="login")
def login():
    if request.method == "GET":
        return render_template("auth/login.html")
    email = request.form.get("email")
    if not email:
        return render_template("auth/login.html", error="email not passed")
    user = UserModel.query.filter_by(email=email).one_or_none()
    if user is None:
        return render_template("auth/login.html", error=f"login please")
    login_user(user)
    return redirect(url_for("index"))


@auth_app.route("/logout/", endpoint="logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))



__all__ = [
    "login_manager",
    "auth_app",
]
