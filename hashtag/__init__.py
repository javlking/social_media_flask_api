from flask import Blueprint
from flask_restx import Api, Resource

# Amina
bp = Blueprint('hashtags', __name__, url_prefix='/hashtag')
api = Api(bp)


@api.route('/')
class CreateOrGetHashTags(Resource):
    # create_hashtag
    def post(self):
        pass

    # get_some_hashtags
    def get(self, size=20, page=1):
        pass


@api.route('/<string:hashtag_name>')
class GetHashTagByName(Resource):
    def get(self, hashtag_name):
        pass

