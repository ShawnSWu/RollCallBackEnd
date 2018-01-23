from flask import Flask
from Login.accountManger import account_Request

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Hello RollCall User"

    app.register_blueprint(account_Request, url_prefix="/accountManger")
    return app