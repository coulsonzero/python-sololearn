from flask import Blueprint, jsonify, request
import pymysql

app_book = Blueprint('book', __name__)
conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='flask_book', charset='UTF8MB4')
cur = conn.cursor()

@app_book.route('/', methods=['GET'])
def get_all_books():
    cur.execute("SELECT * FROM users")
    ans = []
    for row in cur.fetchall():
        ans.append(row)
    return jsonify({
        "code": 200,
        "data": ans,
        "message": "查询所有用户成功"
    })


@app_book.route('/<book_id>', methods=['GET'])
def get_book(book_id):
    cur.execute(f"SELECT * FROM users where id = {book_id};")
    ans = cur.fetchone()

    return jsonify({
        "code": 200,
        "data": ans,
        "message": "查询用户成功"
    })

@app_book.route('/', methods=["POST"])
def add_book():
    username = request.form.get("username")
    password = request.form.get("password")
    cur.execute(f"insert into users(username, password) values {username, password};")

    return jsonify({
        "code": 200,
        "message": "添加用户成功"
    })

# error
@app_book.route('/<book_id>', methods=["PUT"])
def update_book(book_id):
    username = request.form.get("username")
    password = request.form.get("password")
    print(username, password)
    sql = f"update users set username = {username}, password = {password} where id = {book_id};"
    cur.execute(sql)

    return jsonify({
        "code": 200,
        "message": "更新用户成功"
    })

@app_book.route('/<book_id>', methods=["DELETE"])
def delete_book(book_id):
    # 检查id是否存在
    cur.execute("SELECT id FROM users")
    if book_id not in cur.fetchall():
        return '该用户不存在'

    # delete
    cur.execute(f"delete from users where id = {book_id}")
    return jsonify({
        "code": 200,
        "message": "删除用户成功"
    })