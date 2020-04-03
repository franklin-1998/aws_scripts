# for database
import psycopg2
# connecting flask

from flask import request, jsonify,Flask
from flask_cors import CORS,cross_origin

import requests

#initializing postgresql database
conn = psycopg2.connect(database="remote_efficiency_db", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5433")
cur = conn.cursor()



# initializing Flask app
# app config for the flask

app = Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app)

# initialize global variables
headers = {'content-type': 'application/json'}
import ast
from time import sleep,time

cors = CORS(app, resources={r"/register": {"origins": "*"}})
@app.route('/register', methods=['GET','POST'])
def registerForm():
    json_data = ast.literal_eval(request.data.decode('utf-8'))
    current_timestamp = time()
    try:
        cur.execute("INSERT INTO user_credentials (username,companyname,mailid,password,timestamp) VALUES  (%s, %s,%s,%s,%s)",(json_data['name'], json_data['company_name'], json_data['mail_id'],json_data['password'],current_timestamp))
        conn.commit()
        print('\n\n\n Successfully Account Created\n\n\n')
        return {"status":"ok"}
    except:
        return "some error in execution"

app.run(port = 8000,use_reloader = True)
