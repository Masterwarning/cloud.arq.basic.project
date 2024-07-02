from flask import Flask
app = Flask(__name__)
from routes.route import *

local_server = True

if __name__ == '__main__':

    if local_server != True:
        host = "0.0.0.0"
        port = "80"
    else:
        host = "localhost"
        port = "8080"
            
    app.run(host, port)
    #curl http://checkip.amazonaws.com