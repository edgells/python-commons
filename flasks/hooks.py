from flask import Flask, abort, Response

app = Flask(__name__)

app.config['DEBUG'] = False
app.config['JSON_AS_ASCII'] = False


# 在第一次请求前调用
@app.before_first_request
def before_first_request():
    print('first request...')


# 在请求之前调用
@app.before_request
def before_request():
    print("before request")
    return


# 在请求之后调用
@app.after_request
def request_after(response: Response):
    print("request after...")
    response.headers['Content-Type'] = 'application/json'
    return response


# 请每一次请求之后都会调用，会接受一个参数，参数是服务器出现的错误信息
@app.teardown_request
def teardown_request(e):
    print("teardown_request")


@app.route('/')
def index():
    return {"data": "首页"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
