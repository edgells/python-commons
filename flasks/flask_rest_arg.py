from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse


app = Flask(__name__)
api = Api(app)

app.config['DEBUG'] = False
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    return {"data": "首页"}


class ArgsResource(Resource):

    def get(self):
        req = reqparse.RequestParser()

        """
            required: 是否必要参数
            help: 出错的帮助信息
            action: 如果参数多次出现, store 保留第一次出现的参数, append 以list 形式追加
            type: 指定参数类型, flask_restful.input 中提供基本方法, 自定义
                def mobile(mobile_str):
                    if re.match(r'^1[[3-9]\d{9}$', mobile_str):
                        return mobile_str
                    
                    else:
                        raise ValueError('{} is not a valid mobile".format(mobile_str))
                        
                
                rp.add_argument('a', type=mobile)
            
            location: 参数出现的位置
            
        """

        req.add_argument("a", required=True)
        args = req.parse_args()
        return {'msg': 'data={}'.format(args.a)}


api.add_resource(ArgsResource, '/arg/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
