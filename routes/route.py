from controller.control import *
from server import app

@app.route("/")
def index_page():
    return ctrl_home()