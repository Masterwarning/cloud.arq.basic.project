from flask import render_template, request
from database.db import *
from controller.admin_s3 import *

def ctrl_home():
    return render_template("index.html")