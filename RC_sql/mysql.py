import MySQLdb

host = "us-cdbr-iron-east-05.cleardb.net"
user = "bf4c0cc20ecc57"
passwd = "a4f21c13"
db_name = "heroku_135deb52640a216"


def mysql_command(execute_command):
    db = __mysql_connect(execute_command)
    cursor = db.cursor()
    results = cursor.fetchall()
    db.close()
    return results


def mysql_insert_data(execute_command):
    db = __mysql_connect(execute_command)
    db.commit()
    db.close()


def __mysql_connect(execute_command):
    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db_name)
    cursor = db.cursor()
    sql_command = execute_command
    cursor.execute(sql_command)
    return db
