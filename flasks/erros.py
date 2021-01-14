from flask import Flask, abort

app = Flask(__name__)

app.config['DEBUG'] = False
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    return {'data': 'index page'}


@app.route('/error/')
def error():
    abort(500)


# 指定处理异常
@app.errorhandler(500)
def internal_server_error(e):
    return {"data": "服务器搬家了"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
