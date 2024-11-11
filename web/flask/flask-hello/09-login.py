from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")     # templates !
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        print(username, password)
    return redirect("index")

@app.route("/index")
def index():
    return "首页"

if __name__ == '__main__':
    app.run()