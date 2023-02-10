from flask import Blueprint
from flask_restx import Api, Resource


# Imran
bp = Blueprint('comments', __name__, url_prefix='/comment')
api = Api(bp)


@api.route('/<int:post_id>')
class GetOrCreateOrChangeOrDeleteComment(Resource):
    # get_comment_by_post_id
    def get(self, post_id):
        pass

    # create_comment_to_post_by_post_id
    def post(self, post_id):
        pass

    # change_comment_to_post_by_post_id
    def put(self, post_id):
        pass

    # delete_comment_from_post_by_post_id
    def delete(self, post_id):
        pass
