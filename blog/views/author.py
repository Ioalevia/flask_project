from flask import Blueprint, render_template
from blog.models import AuthorModel

authors_app = Blueprint("authors_app", __name__)


@authors_app.route("/", endpoint="list")
def authors_list():
    authors = AuthorModel.query.all()
    return render_template("author/list.html", authors=authors)
