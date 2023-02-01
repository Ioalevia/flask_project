from flask_combo_jsonapi import ResourceDetail, ResourceList
from blog.schemas import ArticleSchema
from blog.models import db
from blog.models import ArticleModel

class ArticleList(ResourceList):
    schema = ArticleSchema
    data_layer = {
    "session": db.session,
    "model": ArticleModel,
    }
class ArticleDetail(ResourceDetail):
    schema = ArticleSchema
    data_layer = {
    "session": db.session,
    "model": ArticleModel,
    }
