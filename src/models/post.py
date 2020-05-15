from . import db
from .author import Author  

#configura modelo de dados do POST
class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True) 
    text = db.Column(db.Text())
    created = db.Column(db.DateTime) 
    author_id = db.Column(
        db.Integer, db.ForeignKey('author.id', ondelete='CASCADE'))
    author = db.relationship('Author')
    subtitle = db.Column(db.String)

    def __str__(self):
        return self.description

    def get_post_id(self):
        return self.id