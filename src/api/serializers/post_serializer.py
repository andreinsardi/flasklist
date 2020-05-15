from flask_restplus import fields
from src.config.restplus import api


post_request = api.model('Post Request', {
    'text': fields.String(required=True, description='text post'),
    'author_id': fields.Integer(required=True, description='post author ID '),
    'subtitle' : fields.String(required=True, description='text subtitle')

})

post_result = api.model('Post Result', {
    'id': fields.Integer(required=True, description='Post Id'),
    'text': fields.String(required=True, description='text post'),
    'author_id': fields.Integer(required=True, description='post author ID'),
    'created': fields.String(required=True, description='date post created'),
    'subtitle' : fields.String(required=True, description='text subtitle')

})
