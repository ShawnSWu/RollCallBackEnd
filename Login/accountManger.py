from flask import Blueprint
from flask import request, abort
import hashlib
import json
from RC_sql.mysql import *
import re

account_Request = Blueprint('loginRequest', __name__)


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


# 補上輸入規則
def auth_account(account, password):
    if validate_email(str(account)) is not True:
        return 'account is not ok'
    else:
        sql_command = "select account from user_info where account = '%s' and password = '%s'" % (
            str(account), str(password))
        result = mysql_command(sql_command)
        rc = len(result)
        if rc is 1:
            return True
        else:
            return False


def validate_email(email):
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) is not None:
            return True
    return False
