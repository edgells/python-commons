from flask import Flask, redirect, url_for

app = Flask(__name__)

# app config
app.config['DEBUG'] = True
app.config['JSON_AS_ASCII'] = False  # 不适用ascii 编码


# 同一个函数可以定义多个路由
@app.route('/')
@app.route('/<int:user_id>/')
def index(user_id=None):
    return {'data': f'首页 {user_id}'}, 222  # 自定义状态码


@app.route('/re/')
def redirects():
    # 重定向
    # return redirect("http://www.baidu.com")
    # url_for 通过endpoint 工作
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
