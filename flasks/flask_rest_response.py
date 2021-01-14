from flask import Flask
from flask_restful import Resource, Api, fields
from flask_restful import marshal_with, marshal


app = Flask(__name__)
api = Api(app)

response_field = {
    'name': fields.String,
    'address': fields.String,
    'user_id': fields.Integer,
}


def decorator(func):
    def wrapper(*args, **kwargs):
        print("decorator running")

        return func(*args, **kwargs)

    return wrapper


class HelloWorldResource(Resource):
    method_decorators = {
        'get': [decorator, ]
    }

    def get(self):
        return {"data": "hello world"}


class UserResource(Resource):

    # 如果不存在的字段会补充null
    @marshal_with(response_field, envelope='resource')
    def get(self):
        return {"name": "laowang", "user_id": 1231231}


class UserProfileResource(Resource):

    def get(self):
        return marshal({"name": "laowang", "user_id": 1231231}, response_field)


api.add_resource(HelloWorldResource, '/', endpoint='HelloWorld')
api.add_resource(UserResource, "/users/")
api.add_resource(UserProfileResource, '/users/profile/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
