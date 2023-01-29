from sqlalchemy import Column, Integer, ForeignKey, String, Text, DateTime, func
from sqlalchemy.orm import relationship
from blog.models import db
from datetime import datetime
from blog.models.article_tag import article_tag_association_table


class ArticleModel(db.Model):
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("author_model.id"))
    author = relationship("AuthorModel", back_populates="articles")
    title = Column(String(200), nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")
    dt_created = Column(DateTime, default=datetime.utcnow, server_default=func.now())
    dt_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    tags = relationship(
        "TagModel",
        secondary=article_tag_association_table,
        back_populates="articles",
    )

    def __str__(self):
        return self.title

