import MySQLdb


def mysql_command(execute_command):
    db = MySQLdb.connect(host="localhost",
                         user="rollcall4shawn", passwd="Mriw%Me^u", db="rollcall_db")
    cursor = db.cursor()
    sql_command = execute_command
    cursor.execute(sql_command)

    results = cursor.fetchall()
    db.close()
    return results
