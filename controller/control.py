from flask import render_template, request
from database.db import *
from controller.admin_s3 import *

def ctrl_index():
    return render_template("index.html")

def ctrl_register_page():
    return render_template("register.html")

def ctrl_consult_page():
    return render_template("consult.html")

def ctrl_register_user():
    rf = request.form
    id = rf['id']
    name = rf['name']
    lastname = rf['lastname']
    email = rf['email']
    telephone = rf['telephone']
    birthday = rf['birthday']
    gender = rf['gender']
    address = rf['address']

    photo = request.files['photo']
    local_path = save_photo(photo)
    
    user_registration = add_user(id, name, lastname, email, telephone, birthday, gender, address)

    if user_registration == True:
        upload_status = upload_s3(local_path, photo, id) 
        if upload_status == True:
            return "Se creo correctamente el usurio: " + id
        else:
            return "Se creo el usurio: " + id + ", foto no valida"        
    else:
            return user_registration


def ctrl_consult_user():   
    obj_user = request.get_json()
    id = obj_user["id"]
    user_data = consult_user(id)

    photo_url = "undefined"

    if user_data == False:
        response = {'status' : 'not found'}
        return response
    elif user_data != None:

        user_photo = consult_file(id)
        if user_photo != None:
            photo_url = user_photo

        response = {
            'status' : 'OK',
            'object' : user_data,
            'photo' : photo_url
        }
        return response
    else:
        response = {'status' : 'error'}
        return response