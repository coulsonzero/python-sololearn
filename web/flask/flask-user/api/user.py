from flask import Blueprint, jsonify, request
import pymysql

app_user = Blueprint('user', __name__)
# mysql
conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='flask_user', charset='UTF8MB4')
cur = conn.cursor()

@app_user.route('/')
def get_users():
    cur.execute("SELECT * FROM users")
    return jsonify({
        "code": 200,
        "data": cur.fetchall(),
        "message": "查询成功"
    })

@app_user.route("/<user_id>")
def get_user(user_id):
    cur.execute(f"SELECT * FROM users where id = {user_id};")
    ans = cur.fetchone()

    return jsonify({
        "code": 200,
        "data": ans,
        "message": "查询成功"
    })


@app_user.route('/', methods=["POST"])
def add_user():
    username = request.form.get("username")
    password = request.form.get("password")
    sql = f"insert into users(username, password) values{username, password};"
    cur.execute(sql)

    return jsonify({
        "code": 200,
        "message": "添加用户成功"
    })

@app_user.route('/<user_id>', methods=["PUT"])
def update_user(user_id):
    name = request.form.get("username")
    psw = request.form.get("password")
    print(name, psw)
    sql = f"update users set username = '{name}', password = '{psw}' where id = {user_id};"
    cur.execute(sql)

    return jsonify({
        "code": 200,
        "data": user_id,
        "message": "更新用户成功"
    })

@app_user.route('/<user_id>', methods=["DELETE"])
def delete_user(user_id):
    cur.execute(f"delete from users where id = {user_id}")
    return jsonify({
        "code": 200,
        "data": user_id,
        "message": "删除用户成功"
    })