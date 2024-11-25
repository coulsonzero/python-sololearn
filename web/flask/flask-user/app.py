from flask import Flask
from api.user import user

app = Flask(__name__)
# 识别中文，防止乱码
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(user, url_prefix='/user')


@app.route('/')
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()