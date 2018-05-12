from flask import Flask
from Login.accountManger import account_Request
from ListData.ListApi import list_Request
from ToDo_NoteAPI.ToDoApi import todo_request


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Hello RollCall User"

    app.register_blueprint(account_Request, url_prefix="/account")
    app.register_blueprint(list_Request, url_prefix="/list")
    app.register_blueprint(todo_request, url_prefix="/todo")
    return app
