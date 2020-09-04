from flask import Flask
from flask import request, jsonify
from wit import Wit

import tools as tools

app = Flask(__name__)
access_token = "DLOQL2S3S3TBYYULATBVYJDISSNM7BKS"

client = Wit(access_token)



@app.route('/', methods=['POST'])
def listening():
  data = request.json
  resp = client.message(data['question'])
  tools.read_text(tools.choose_response(resp["intents"][0]["name"]))
  return {
    "status": "END",
    "request": data['question'],
    "response": resp
  }

@app.route('/hello', methods=['GET'])
def hello():
  return "COUCOU"