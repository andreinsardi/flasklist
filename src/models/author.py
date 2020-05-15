from . import db 

#configura modelo de dados do AUTHOR
class Author(db.Model):
    __tablename__ = 'author'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255)) 
    age = db.Column(db.Integer)


    def __str__(self):
        return self.first_name

    def get_user_id(self):
        return self.id

  

