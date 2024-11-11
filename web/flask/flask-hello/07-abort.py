from flask import Flask, request, abort

app = Flask(__name__)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return "this is get request."
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "shville" and password == "admin123":
            return "success to login"
        else:
            abort(404)
            return None


if __name__ == '__main__':
    app.run()

