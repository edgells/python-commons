from flask import Flask, request, current_app

"""
    flask context
    request: 当有请求进入的时候, flask 框架会在全局的stack 中压入一个 request context
    current_app: 同时也会将 app context 压入stack 中
    
"""


app = Flask(__name__)

app.config['DEBUG'] = False
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():

    return {"data": "首页"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
