from flask import Flask, request, g, render_template
from time import time
from werkzeug.exceptions import BadRequest
from blog.user.views import user
from blog.article.views import article

app: Flask = Flask(__name__)
app.register_blueprint(user)
app.register_blueprint(article)

@app.route('/')
def index():
    return render_template(
        'index.html',
    )
# def create_app() -> Flask:
#     app = Flask(__name__)
#     register_blueprints(app)
#     return app
#
# def register_blueprints(app: Flask):
#     app.register_blueprint(user)
#     app.register_blueprint(article)
