from flask_restplus import fields
from src.config.restplus import api
from src.api.serializers.post_serializer import post_result


author_request = api.model('Author Request', {
    'first_name': fields.String(required=True, description='text post') ,
    'last_name': fields.String(required=True, description='text post'),
    'age' : fields.Integer(required=True, description='int age') 
})

author_result = api.model('Author Result', {
    'id': fields.Integer(required=True, description='Post Id'),
    'first_name': fields.String(required=True, description='text post'), 
    'last_name': fields.String(required=True, description='text post'),
    'age' : fields.Integer(required=True, description='int age') 
})

author_post_result = api.model('Author Post Result', {
    'id' : fields.Integer(required=True, description='Post Id'),
    'first_name': fields.String(required=True, description='text post'), 
    'last_name': fields.String(required=True, description='text post'),
    'age' : fields.Integer(required=True, description='int age'),
    'listPosts' : fields.List(fields.Nested(post_result), description='list posts')
})
