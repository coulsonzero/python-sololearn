from flask import Flask

app = Flask(__name__)


@app.route('/hello', methods=["GET"])
def hello():
    return "hello flask."

@app.route('/hi', methods=["POST"])
def hi():
    return "hi flask."



if __name__ == '__main__':
    app.run()
