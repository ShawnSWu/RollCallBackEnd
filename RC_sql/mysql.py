import MySQLdb


def mysql_command(execute_command):
    db = MySQLdb.connect(host="us-cdbr-iron-east-05.cleardb.net",
                         user="bf4c0cc20ecc57", passwd="a4f21c13", db="heroku_135deb52640a216")
    cursor = db.cursor()
    sql_command = execute_command
    cursor.execute(sql_command)

    results = cursor.fetchall()
    db.close()
    return results
