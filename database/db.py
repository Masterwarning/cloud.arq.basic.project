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
        print("db.connectionSQL: Error -", error)
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
            print("db.add_user: ID - " + id)
            return True
        return False
    except Exception as error:
        print("db.add_user: Error -", error)
        return False