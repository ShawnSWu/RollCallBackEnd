from flask import Flask
from Login.accountManger import account_Request
from ListData.ListApi import list_Request

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Hello RollCall User"

    app.register_blueprint(account_Request, url_prefix="/account")
    app.register_blueprint(list_Request, url_prefix="/list")
    return app
