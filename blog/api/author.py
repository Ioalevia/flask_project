from flask_combo_jsonapi import ResourceDetail, ResourceList
from blog.schemas import AuthorSchema
from blog.models.database import db
from blog.models import AuthorModel, ArticleModel
from combojsonapi.event.resource import EventsResource

class AuthorDetailEvents(EventsResource):
    def event_get_articles_count(self, **kwargs):
        return {"count": ArticleModel.query.filter(ArticleModel.author_id == kwargs["id"]).count()}

class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
    "session": db.session,
    "model": AuthorModel,
    }
class AuthorDetail(ResourceDetail):
    events = AuthorDetailEvents
    schema = AuthorSchema
    data_layer = {
    "session": db.session,
    "model": AuthorModel,
    }