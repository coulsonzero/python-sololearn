from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=False)
