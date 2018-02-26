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

    return json.dumps(return_json_dict, ensure_ascii=False)


@list_Request.route("/insertnewlist", methods=['POST'])
def insert_new_List():
    if not request.json:
        abort(404)

    json_dict = request.json
    account = json_dict['account']
    return_message = None
    # 檢查是否重複
    new_list_name = json_dict['new_list_name']
    if __auth_if_repeat_list(account, new_list_name) is False:
        sql_command = "insert into user_list_info values ('%s', '%s', '', '') " % (str(account), str(new_list_name))

        insert_result = mysql_command(sql_command)
        if insert_result is True:
            return_message = 'insert Success'
        else:
            return_message = 'insert Fail (SQL Error)'

    else:
        return_message = 'Repeat List'

    return json.dumps(return_message, ensure_ascii=False)


def __auth_if_repeat_list(account, new_list_name):
    # 如果有重複 返回True 沒有重複返回False
    sql_command = "select listname from user_list_info where account = '%s' and listname = '%s'" % (
        str(account), str(new_list_name))
    rowcount = get_row_count(sql_command)

    if rowcount >= 1:
        return True
    else:
        return False


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
    group_image_uri = json_dict['group_image_uri']

    return_message = None

    insert_result = None

    if insert_type != "extra_add":
        # another new_add,change_add 都一樣 先刪除 在全部加入
        __delete_list_data(account, list_name)


    a = None

    b = None

    c = None

    d = None

    for data in data_list:
        # data type is dictionary
        for key in data.keys():
            sql_command = " insert into user_list_info values ('%s', '%s', '%s', '%s', '%s') " % (str(account), str(list_name), str(key), str(data[key]), str(group_image_uri))
            result = mysql_command(sql_command)


            insert_result = result

    if insert_result is True:
        return_message = 'insert Success'
    else:
        return_message = 'insert Fail (SQL Error)'+a+' '+b+' '+c+' '+d

    return json.dumps(return_message, ensure_ascii=False)


def __delete_list_data(account, list_name):
    sql_command = "select * from user_list_info where account = '%s' and listname = '%s'" % (account, list_name)
    select_result = get_row_count(sql_command)

    if select_result >= 1:
        sql_command = "delete from user_list_info where account = '%s' and listname = '%s' " % (account, list_name)
        mysql_command(sql_command)


@list_Request.route("/getalllistdata", methods=['POST'])
def get_all_list_data():
    if not request.json:
        abort(404)

    # 撈資料 select listname,count(listkey) as people_count,group_image_code from user_list_info where account = 'swshawnwu@gmail.com' group by listname

    # 改圖片 update user_list_info SET group_image_uri = 'https://i.imgur.com/oKTl5Ka.jpg' where account = 'swshawnwu@gmail.com' and listname = '美國團'

    json_dict = request.json
    account = json_dict['account']
    sql_command = "select listname,count(listkey)-1 as people_count,group_image_uri from user_list_info where account = '%s' group by listname" % (
        str(account))

    result = get_mysql_data(sql_command)

    return_list = []

    if result is not None:
        for data in result:
            print(data)
            item_json = {'listname': data[0], 'people_count': data[1], 'group_image_uri': data[2]}
            return_list.append(item_json)

    return json.dumps(return_list, ensure_ascii=False)


@list_Request.route("/creategroup", methods=['POST'])
def create_group():
    if not request.json:
        abort(404)

    json_dict = request.json
    account = json_dict['account']
    listname = json_dict['listname']
    group_image_uri = json_dict['group_image_uri']

    sql_command = "insert into user_list_info values ('%s','%s','','','%s')" % (str(account), str(listname), str(group_image_uri))

    result = mysql_command(sql_command)

    return json.dumps(result, ensure_ascii=False)


@list_Request.route("/deletegroup", methods=['POST'])
def delete_group():
    if not request.json:
        abort(404)

    json_dict = request.json
    account = json_dict['account']
    listname = json_dict['listname']

    sql_command = "delete from user_list_info where account = '%s' and listname = '%s'" % (str(account), str(listname))

    result = mysql_command(sql_command)

    return json.dumps(result, ensure_ascii=False)