from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = False
app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = 'demo is 18'


@app.route('/')
def index():
    return {"data": "首页"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
