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
    return json.dumps(auth_account(account, sha256_password))


def auth_account(account, password):
    if validate_email(str(account)) is not True:
        return 'account is not ok'
    else:
        sql_command = "select account from user_info where account = '%s' and password = '%s'" % (
            str(account), str(password))
        result = mysql_command(sql_command)
        rc = len(result)
        # 1 equals only a data
        if rc is 1:
            return True
        else:
            return False


def validate_email(email):
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) is not None:
            return True
    return False


@account_Request.route("/signup", methods=['POST'])
def signup():
    if not request.json:
        abort(404)

    json_dict = request.json
    signup_account = json_dict['signup_account']
    signup_password = json_dict['signup_password']
    signup_name = json_dict['signup_name']

    signup_password.encode('utf-8')
    sha256_password = hashlib.sha256(str(signup_password).encode('utf-8')).hexdigest()

    signup_account_if_ok = auth_if_repeat_account(signup_account)
    # 沒重複帳號 返回false
    if signup_account_if_ok is False:
        sql_command = "insert into user_info values ('%s','%s','%s')" % (str(signup_account),
                                                                         str(sha256_password), str(signup_name))
        mysql_command(sql_command)
        return json.dumps('Signup Success')
    else:
        return json.dumps('Signup Fail')


def auth_if_repeat_account(signup_account):
    if validate_email(str(signup_account)) is not True:
        return 'account is not ok'
    else:
        sql_command = "select account from user_info where account = '%s'" % (
            str(signup_account))
        result = mysql_command(sql_command)
        rc = len(result)
        # 0 equals no any repeat data
        if rc is 0:
            return False
        else:
            return True


