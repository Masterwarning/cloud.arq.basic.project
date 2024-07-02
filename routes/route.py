from controller.control import *
from server import app

@app.route("/")
def index_page():
    return ctrl_index()

@app.route("/registrar")
def register_page():
    return ctrl_register_page()

@app.route("/consultar")
def consult_page():
    return ctrl_consult_page()

@app.route("/register_user", methods=['post'])
def register_user():
    return ctrl_register_user()