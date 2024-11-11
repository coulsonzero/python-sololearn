from flask import Flask, redirect, url_for
app = Flask(__name__)


@app.route("/index")
def index():
    return redirect("https://cn.bing.com")

@app.route("/hello")
def hello():
    return "hello, flask"

@app.route("/hi")
def hi():
    # return redirect(url_for("hello"))
    return redirect("hello")

if __name__ == '__main__':
    app.run()