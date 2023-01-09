from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound

article_app = Blueprint("article_app", __name__)


ARTICLES = {
    1: {'name': 'delete', 'author': {'id': 1, 'name': 'root'}},
    2: {'name': 'live', 'author': {'id': 2, 'name': 'user1'}},
    3: {'name': 'create', 'author': {'id': 3, 'name': 'user2'}}
}

@article_app.route("/", endpoint="list")
def article_list():
    return render_template("article/list.html", articles=ARTICLES)

@article_app.route('/<int:pk>')
@login_required
def get_article(pk: int):
    try:
        article_name = ARTICLES[pk]
    except KeyError:
        raise NotFound(f'Article id {pk} not found.')
        # return redirect('/users/')
    return render_template(
        'article/detail.html',
        article_name=article_name,
    )