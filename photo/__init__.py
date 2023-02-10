from flask import Blueprint

from flask_restx import Api, Resource


# Muhammadamin
bp = Blueprint('photo', __name__, url_prefix='/photo')
api = Api(bp)


@api.route('/')
class GetAllPhotosOrCreate(Resource):
    # get_all_photos
    def get(self):
        pass

    # create_photo
    def post(self):
        pass


@api.route('/<int:photo_id>')
class GetOrChangeOrDeletePostById(Resource):
    # get_photo_by_id
    def get(self, photo_id):
        pass

    # change_photo_by_id
    def put(self, photo_id):
        pass

    # delete_photo_by_id
    def delete(self, photo_id):
        pass

