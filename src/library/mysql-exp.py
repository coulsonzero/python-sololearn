import pymysql


def doSQL(sql):
    cursor.execute(sql)
    conn.commit()

if __name__ == '__main__':
    conn = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="py_learn",
        charset="UTF8MB4"
    )
    cursor = conn.cursor()
    doSQL("drop database if exists py_learn;")
