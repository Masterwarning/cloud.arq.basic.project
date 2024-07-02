from flask import render_template, request
from database.db import *
from controller.admin_s3 import *

def ctrl_index():
    return render_template("index.html")

def ctrl_register_page():
    print("control")
    return render_template("register.html")

def ctrl_consult_page():
    return render_template("consult.html")

def ctrl_register_user():
    rf = request.form
    id = rf['id']
    name = rf['name']
    lastname = rf['lastname']
    email = rf['email']
    birthday = rf['birthday']
    gender = rf['gender']
    address = rf['address']
    user_registration = add_user(id, name, lastname, email, birthday, gender, address)
    test = str(user_registration)
    print(test)
    return test