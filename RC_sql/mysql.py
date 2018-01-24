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
    cursor.execute(sql_command)
    results = cursor.fetchall()
    db.commit()
    db.close()
    return results

