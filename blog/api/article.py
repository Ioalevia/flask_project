from flask_combo_jsonapi import ResourceDetail, ResourceList
from blog.schemas import ArticleSchema
from blog.models import db
from blog.models import ArticleModel
from combojsonapi.event.resource import EventsResource

class ArticleListEvents(EventsResource):
    def event_get_count(self, *args, **kwargs):
        return {"count": ArticleModel.query.count()}

class ArticleList(ResourceList):
    events = ArticleListEvents
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
