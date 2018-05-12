from flask import Blueprint
from flask import request, abort
from RC_sql.mysql import *
import json

todo_request = Blueprint('todo_request', __name__)


@todo_request.route("/gettododate", methods=['POST'])
def get_todo_data():
    if not request.json:
        abort(404)

    json_dict = request.json
    account = json_dict['account']
    password = json_dict['password']
    sql_command = "select todo_title,todo_createtime,todo_isFinsh from todo_note where account = '%s' " % (
        str(account))
    result = get_mysql_data(sql_command)

    return_list = []

    if result is not None:
        for data in result:
            item_json = {'todo_title': data[0], 'todo_createtime': data[1], 'todo_isFinsh': data[2]}
            return_list.append(item_json)

    return json.dumps(return_list, ensure_ascii=False)


@todo_request.route("/createnewtodo", methods=['POST'])
def create_new_todo():
    if not request.json:
        abort(404)

    json_dict = request.json
    account = json_dict['account']
    password = json_dict['password']
    todo_title = json_dict['todo_title']
    todo_createtime = json_dict['todo_createtime']

    sql_command = "insert into todo_note values('%s','%s','%s', 0) " % (
        str(account), str(todo_title), str(todo_createtime))
    result = mysql_command(sql_command)

    return json.dumps(result, ensure_ascii=False)


@todo_request.route("/updatefinshtodo", methods=['POST'])
def finsh_todo():
    if not request.json:
        abort(404)

    json_dict = request.json
    account = json_dict['account']
    password = json_dict['password']
    todo_title = json_dict['todo_title']
    todo_isFinsh = json_dict['todo_isFinsh']

    sql_command = "update todo_note set todo_isFinsh = %d where account = '%s' and todo_title = '%s' " % (todo_isFinsh,
        str(account), str(todo_title))
    result = mysql_command(sql_command)

    return json.dumps(result, ensure_ascii=False)