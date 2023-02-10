from flask import Blueprint
from flask_restx import Resource, Api, fields


bp = Blueprint('users', __name__, url_prefix='/user')

# Регистрируем как swagger
api = Api(bp)


@api.route('/')
class GetAllUserOrCreate(Resource):
    # Для получения пользователей
    def get(self):
        pass

    # Для регистрации
    def post(self):
        pass


@api.route('/<int:user_id>')
class GetExactUser(Resource):
    def get(self, user_id):
        pass


@api.route('/<int:photo_id>')
class ChangeOrDeleteUserPhoto(Resource):
    # Изменить аватарку
    def put(self, photo_id):
        pass

    # Удалить аватарку
    def delete(self, photo_id):
        pass


