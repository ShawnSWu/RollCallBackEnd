from flask import Blueprint
from flask import request, abort
from RC_sql.mysql import *
import hashlib, json, re

account_Request = Blueprint('account_request', __name__)


@account_Request.route("/login", methods=['POST'])
def login():
    if not request.json:
        abort(404)

    json_dict = request.json
    account = json_dict['account']
    password = json_dict['password']
    password.encode('utf-8')
    sha256_password = hashlib.sha256(str(password).encode('utf-8')).hexdigest()
    print(sha256_password)
    return json.dumps(auth_account(account, sha256_password), ensure_ascii=False)


def validate_email(email):
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) is not None:
            return True
    return False


def auth_account(account, sha256_password):
    if validate_email(str(account)) is not True:
        return 'account is not ok'
    else:
        sql_command = "select account from user_info where account = '%s' and password = '%s'" % (
            str(account), str(sha256_password))
        rowcount = get_row_count(sql_command)
        # 1 equals only a data
        return rowcount == 1


@account_Request.route("/signup", methods=['POST'])
def signup():
    if not request.json:
        abort(404)

    json_dict = request.json
    signup_account = json_dict['signup_account']
    signup_password = json_dict['signup_password']
    signup_name = json_dict['signup_name']
    profile_image = json_dict['profile_image']

    signup_name.encode('utf-8')
    sha256_password = hashlib.sha256(str(signup_password).encode('utf-8')).hexdigest()
    return_message = None

    # 沒重複帳號 返回false
    signup_account_if_ok = auth_if_repeat_account(signup_account)
    if signup_account_if_ok is False:
        sql_command = "insert into user_info values ('%s','%s','%s','%s')" % (str(signup_account),
                                                                         str(sha256_password), str(signup_name), str(profile_image))
        insert_result = mysql_command(sql_command)
        if insert_result is True:
            return_message = 'Signup Success'
        else:
            return_message = 'Signup Fail'
    else:
        return_message = 'repeat account'

    return json.dumps(return_message, ensure_ascii=False)


def auth_if_repeat_account(signup_account):
    if validate_email(str(signup_account)) is not True:
        return 'account is not ok'
    else:
        sql_command = "select account from user_info where account = '%s'" % (
            str(signup_account))
        rowcount = get_row_count(sql_command)
        # 0 equals no any repeat data
        return rowcount == 0

@account_Request.route("/getprocfiledata", methods=['POST'])
def get_procfile_data():
    if not request.json:
        abort(404)

    json_dict = request.json
    account = json_dict['account']
    password = json_dict['password']

    sql_command = "select account,name,profile_image from user_info where account = '%s'" % account

    insert_result = get_mysql_data(sql_command)

    userEmail = insert_result[0][0]
    userName = insert_result[0][1]
    userProfileImage = insert_result[0][2]

    return_json_type = {'userName': userName, 'userEmail': userEmail, 'userProfileImage': userProfileImage}

    print(type(return_json_type))

    return json.dumps(return_json_type, ensure_ascii=False)


@account_Request.route("/getprocfilegroupdevicedate", methods=['POST'])
def get_procfile_group_and_deivce_data():
    if not request.json:
        abort(404)

    json_dict = request.json
    account = json_dict['account']
    password = json_dict['password']

    sql_command = "select count(listname)-1 from user_list_info where account = '%s' group by listname" % account

    insert_result = get_mysql_data(sql_command)

    return_list = []

    if insert_result is not None:
        for data in insert_result:
            return_list.append(data[0])

    return json.dumps(return_list, ensure_ascii=False)


@account_Request.route("/saveprofileimage", methods=['POST'])
def save_profile_image():
    if not request.json:
        abort(404)

    json_dict = request.json
    account = json_dict['account']
    password = json_dict['password']
    profile_image = json_dict['profile_image']

    sql_command = "update user_info SET profile_image = '%s' where account = '%s'" % (profile_image, account)

    insert_result = mysql_command(sql_command)

    return json.dumps(insert_result, ensure_ascii=False)