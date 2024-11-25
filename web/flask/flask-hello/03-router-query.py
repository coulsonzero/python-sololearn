from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


# /hello?name=john
@app.route("/hello")
def hello():
    name = request.args.get("name")
    print(name)
    return f"hello flask! {name}"

if __name__ == '__main__':
    app.run()