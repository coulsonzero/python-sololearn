from flask import Flask
from api.book import app_book

app = Flask(__name__)
# 识别中文，防止乱码
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(app_book, url_prefix="/book")

@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = '8080', debug = True)

