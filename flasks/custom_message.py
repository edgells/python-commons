from flask import Flask
from flask_restful import Resource, Api
from flask_restful import marshal, fields

app = Flask(__name__)
api = Api(app)

app.config['DEBUG'] = False
app.config['JSON_AS_ASCII'] = False


@api.representation('application/json')
def handler_json(data, code, headers):
    return data


class HelloWorldResource(Resource):
    response_fields = {
        'name': fields.String,
        'age': fields.Integer
    }

    def get(self):
        return marshal({'name': 'laowang', 'age': 18}, self.response_fields)


api.add_resource(HelloWorldResource, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
