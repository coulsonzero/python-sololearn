from flask import Flask, request

app = Flask(__name__)


@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return "this is get method."
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # print(username, password)
        return "this is post method. user: {0}, password: {1}".format(username, password)

if __name__ == '__main__':
    app.run()