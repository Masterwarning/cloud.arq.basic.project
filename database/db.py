import pymysql

db_host = "db-project-cloudvet.cn0y60gyiahs.us-east-1.rds.amazonaws.com"
db_user = "admin"
db_password = "r332HQD2TayRtQOG"
db_database = "project_cloudvet"

def connectionSQL():
    try:
        connection_sql = pymysql.connect(
            host = db_host,
            user = db_user,
            password = db_password,
            database = db_database
        )
        print("db.connectionSQL: Established")
        return connection_sql
    except Exception as error:
        print("db.connectionSQL: error -", error)
        return None
    
def add_user(id, name, lastname, email, birthday, gender, address):
    query = "INSERT INTO users(id, name, lastname, email, birthday, gender, address) VALUES ({}, \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\');".format(id, name, lastname, email, birthday, gender, address)
    #print(query)
    connection_sql = connectionSQL()

    try:
        if(connection_sql != None):
            cursor = connection_sql.cursor()
            cursor.execute(query)
            connection_sql.commit()
            print("db.add_user: registrado - " + id)
            return True
        return "Servicios no disponibles, contactar soporte."
    except Exception as error:
        print("db.add_user: error -", error)        
        return "No se puede crear el usuario, verifique los datos"
    

def consult_user(id):
    query = "SELECT * FROM users WHERE id = {};".format(id)
    #print(query)
    connection_sql = connectionSQL()

    try:
        if connection_sql != None:
            cursor = connection_sql.cursor()
            cursor.execute(query)
            user_data = cursor.fetchone()
            if user_data != None:
                print("db.consult_user: encontrado - " + id)
                return user_data
            else:
                print("db.consult_user: error, usuario con id {} no encontrado".format(id))
                return False
        else:
            print("db.consult_user: error, conexion no exitosa")
            return None

    except Exception as error:
        print("db.consult_user: error -", error)
        return None
