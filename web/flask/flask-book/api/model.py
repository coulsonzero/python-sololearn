import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='flask_book', charset='UTF8MB4')
cur = conn.cursor()
def doSQL(sql):
    cur.execute(sql)
    conn.commit()

sql = "SELECT * FROM users"
cur.execute(sql)
for row in cur.fetchall():
    print(row)

cur.close()
conn.close()