import os
from flask import Flask, render_template
from werkzeug.exceptions import BadRequest
from blog.models import db, UserModel
from blog.views.user import users_app
from blog.views.article import article_app
from blog.views.auth import auth_app, login_manager
from flask_migrate import Migrate
from blog.security import flask_bcrypt


app: Flask = Flask(__name__)


cfg_name = "DevConfig"
app.config.from_object(f"blog.config.{cfg_name}")


db.init_app(app)
login_manager.init_app(app)


migrate = Migrate(app,db, compare_type=True)


flask_bcrypt.init_app(app)


@app.cli.command("create-admin")
def create_admin():

    admin = UserModel(username="root",email="123", is_staff=True)
    admin.password = "root"
    db.session.add(admin)
    db.session.commit()
    print("created admin:", admin)


app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(article_app, url_prefix="/articles")
app.register_blueprint(auth_app, url_prefix="/auth")


@app.route("/")
def index():
    return render_template("index.html")
