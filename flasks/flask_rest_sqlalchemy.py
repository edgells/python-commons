from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

app.config['DEBUG'] = True

api = Api(app)


class IndexResource(Resource):
    response_field = {

    }

    def get(self):
        return {
            'data': 'test'

        }


api.add_resource(IndexResource, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
