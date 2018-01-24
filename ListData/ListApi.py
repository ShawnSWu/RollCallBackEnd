from flask import Blueprint
from flask import request, abort
from RC_sql.mysql import *
import hashlib, json, re

list_Request = Blueprint('list_request', __name__)

@list_Request.route("/getlistdata", methods=['POST'])
def get_list_data():
    if not request.json:
        abort(404)

    json_dict = request.json
    account = json_dict['account']
    list_name = json_dict['list_name']
    sql_command = "select listkey ,listvalue from user_list_info where account = '%s' and listname = '%s' " % (str(account), str(list_name))
    result = mysql_command(sql_command)

    for data in result:
        list_key = data[0]
        list_value = data[1]
    # -- 回傳json
    return json.dumps(result)


# 新增List
# 修改List
# 少data_list
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

    if insert_type != "extra_add":
        # another new_add,change_add 都一樣 先刪除 在全部加入
        __delete_list_data(account, list_name)

    for data in data_list:
        # data type is dictionary
        for key in data.keys():
            sql_command = "insert into user_list_info values ('%s', '%s', '%s', '%s')" % (str(account), str(list_name), str(key), str(data[key]))
            mysql_command(sql_command)

    return json.dumps('insert Success')


def __delete_list_data(account, list_name):
    sql_command = "select * from user_list_info where account = '%s' and listname = '%s'"% (account, list_name)
    result = mysql_command(sql_command)
    print(len(result))

    if len(result) is not 0:
        sql_command = "delete from user_list_info where account = '%s' and listname = '%s' " % (account, list_name)
        mysql_command(sql_command)
