import requests
import json
# initialize global variables
headers = {'content-type': 'application/json'}

requests.post("http://127.0.0.1:8000/register",data= json.dumps({"name":"frank","company_name":"Cloobot","mail_id":"frank@cloobot.com","password":"dfdsfa"}),headers=headers)
                                       