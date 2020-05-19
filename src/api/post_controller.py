from flask import request
from flask_restplus import Resource
from src.config.restplus import api
from src.api.serializers.post_serializer import post_request, post_result
from src.services.post_service import create, change, delete, get, get_all
 

ns = api.namespace('api/post', description='Operations related to post')


@ns.route('')#refine rota
class PostCollection(Resource):
    @api.expect(post_request)#define parametro de entrada para a documentaçao do swagger
    @api.marshal_with(post_result)#define resultado da metodo 
    def post(self):
        """
        Create a new posts
        """ 
        post = create(request.json)
        return post 
    
    @api.marshal_with(post_result)#define resultado da metodo 
    def get(self):
        """
        Get all posts
        """
        post = get_all()
        
        return post


 

@ns.route('/<int:id>')
class PostIDCollection(Resource): 
    @api.marshal_with(post_result)
    def get(self, id):
        """
        Get post by ID
        """ 
        post = get(id)
        return post 


    @api.expect(post_request)
    @api.marshal_with(post_result)
    def put(self, id):
        """
        Change post by ID
        """ 
        post = change(id,request.json)
        return post 
 
    @api.marshal_with(post_result)
    def delete(self, id):
        """
        Delete post by ID
        """ 
        post = delete(id)
        return post 