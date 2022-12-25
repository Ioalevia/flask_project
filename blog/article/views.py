from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = {
    1: {'name': 'delete', 'author': {'id': 1, 'name': 'user1'}},
    2: {'name': 'live', 'author': {'id': 2, 'name': 'Alice'}},
    3: {'name': 'create', 'author': {'id': 3, 'name': 'Hanna'}}
}


@article.route('/')
def article_list():
    return render_template(
        'articles/list.html',
        articles=ARTICLES,

    )

@article.route('/<int:pk>')
def get_article(pk: int):
    try:
        article_name = ARTICLES[pk]
    except KeyError:
        raise NotFound(f'Article id {pk} not found.')
        # return redirect('/users/')
    return render_template(
        'articles/details.html',
        article_name=article_name,
    )
