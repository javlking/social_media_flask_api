from flask import Blueprint
from flask_restx import Api, Resource

# Muhammadkhon

bp = Blueprint('posts', __name__, url_prefix='/post')
api = Api(bp)


@api.route('/')
class GetAllPostsOrCreate(Resource):
    # Get all posts
    def get(self):
        pass

    # Create post
    def post(self):
        pass


@api.route('/<int:post_id>')
class GetOrChangeOrDeletePost(Resource):
    # get_post_by_id
    def get(self, post_id):
        pass

    # change_post_by_id
    def put(self, post_id):
        pass

    # delete_post_by_id
    def delete(self, post_id):
        pass



