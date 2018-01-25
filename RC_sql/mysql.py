import MySQLdb

host = "us-cdbr-iron-east-05.cleardb.net"
user = "bf4c0cc20ecc57"
passwd = "a4f21c13"
db_name = "heroku_135deb52640a216"
charset = "utf8"


def mysql_command(execute_command):
    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db_name, charset=charset)
    cursor = db.cursor()
    sql_command = execute_command
    is_success = None
    try:
        cursor.execute(sql_command)
        cursor.fetchall()
        db.commit()
        is_success = True
    except MySQLdb.Error:
        db.rollback()
        is_success = False
    finally:
        db.close()

    return is_success


def get_row_count(execute_command):
    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db_name, charset=charset)
    cursor = db.cursor()
    sql_command = execute_command
    try:
        cursor.execute(sql_command)
        rowcount = cursor.rowcount
        db.commit()
        return rowcount
    except MySQLdb.Error:
        db.rollback()
        return False
    finally:
        db.close()


def get_mysql_data(execute_command):
    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db_name, charset=charset)
    cursor = db.cursor()
    sql_command = execute_command
    result = None
    try:
        cursor.execute(sql_command)
        result = cursor.fetchall()
        db.commit()
    except MySQLdb.Error:
        db.rollback()
    finally:
        db.close()

    return result