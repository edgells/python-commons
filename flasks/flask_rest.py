from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


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


api.add_resource(HelloWorldResource, '/', endpoint='HelloWorld')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
