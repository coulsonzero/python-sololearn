from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False     # 识别中文，防止乱码


@app.route("/user")
def user():
    data = {
        "username": "赵云",
        "password": "admin123"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run()