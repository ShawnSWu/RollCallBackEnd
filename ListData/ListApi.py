from flask import Blueprint
from flask import request, abort
from RC_sql.mysql import *
import json

list_Request = Blueprint('list_request', __name__)


@list_Request.route("/getlistdata", methods=['POST'])
def get_list_data():
    if not request.json:
        abort(404)

    json_dict = request.json
    account = json_dict['account']
    list_name = json_dict['list_name']
    sql_command = "select listkey ,listvalue from user_list_info where account = '%s' and listname = '%s' " % (
        str(account), str(list_name))
    result = get_mysql_data(sql_command)

    return_json_dict = dict()

    for data in result:
        list_key = data[0]
        list_value = data[1]
        return_json_dict[list_key] = list_value

    return json.dumps(return_json_dict)


@list_Request.route("/insertnewdatatolist", methods=['POST'])
def insert_newData_to_oldList():
    if not request.json:
        abort(404)

    json_dict = request.json
    insert_type = json_dict['insert_type']
    account = json_dict['account']
    list_name = json_dict['list_name']
    # data_list type is list
    data_list = json_dict['data_list']

    return_message = None

    if insert_type != "extra_add":
        # another new_add,change_add 都一樣 先刪除 在全部加入
        __delete_list_data(account, list_name)

    sql_command = "insert into user_list_info values "

    for data in data_list:
        # data type is dictionary
        for key in data.keys():
            sql_command += " ('%s', '%s', '%s', '%s') ," % (str(account), str(list_name), str(key), str(data[key]))
    sql_command = sql_command[:-1]

    insert_result = mysql_command(sql_command)
    if insert_result is True:
        return_message = 'insert Success'
    else:
        return_message = 'insert Fail (SQL Error)'

    return json.dumps(return_message)


def __delete_list_data(account, list_name):
    sql_command = "select * from user_list_info where account = '%s' and listname = '%s'" % (account, list_name)
    select_result = get_row_count(sql_command)

    if select_result >= 1:
        sql_command = "delete from user_list_info where account = '%s' and listname = '%s' " % (account, list_name)
        mysql_command(sql_command)

