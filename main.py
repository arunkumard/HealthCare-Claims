from flask import Flask, jsonify
from threading import Thread
from flask_restful import Resource, Api
import json
import random

app = Flask('')
api = Api(app)

@app.route('/')
def home():
  return "I'm alive"


#################################
##API USING FLASK-RESTFUL

class Test(Resource):
  def get(self):
    return jsonify({"Type": "flask-restful"})


def get_orders(claim):
  if claim == "institutional":
    file_address = 'Claims/institutional.json'
  else:
    file_address = 'errormsg.json'  
  with open(file_address, 'r') as claimfile:
    data = json.load(claimfile)
  claim = random.choice(list(data['Claims']))

  return claim 


class Claims(Resource):
  def get(self, claim_type):
    return get_orders(claim_type)

api.add_resource(Claims, '/claims/<string:claim_type>')

def run():
  app.run(host='0.0.0.0',port=7210)

  
t = Thread(target=run)
t.start()