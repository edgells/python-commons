from flask import Flask
from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):

    def __init__(self, url_map, *args):
        super(RegexConverter, self).__init__(url_map)
        self.regex = args[0]

    def to_python(self, value):
        """
        匹配到的值
        :param value:
        :return:
        """
        return int(value)

    def to_url(self, value):
        """
        使用 url for 取获取视图时所对应的url
        :param value:
        :return:
        """
        pass


app = Flask(__name__)
app.config['DEBUG'] = True
app.url_map.converters['re'] = RegexConverter


@app.route('/user/<re("[0-9]{3}"):user_id>/')
def users(user_id):
    return {'data': "user_id: %s" % user_id}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
