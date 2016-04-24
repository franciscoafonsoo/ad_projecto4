from flask import Flask
from flask import request
from flask import json
import sqlite3
import skel
import json
from collections import OrderedDict

app = Flask(__name__)



@app.route('/')
def hello_world():
    return {"Hello": "World"}

@app.route('/messages', methods=['POST'])
def api_message():

    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"
    else:
        return "415 Unsupported Media Type ;)"

@app.route("/alunos", methods=["POST"])
def alunos_api():

    print request.path
    print json.loads(request.data, object_pairs_hook=OrderedDict)
    return "Ok"

@app.route("/turmas", methods=["POST"])
def turmas_api(path):

    if request.method == "PUT":
        pass
    elif request.method == "DELETE":
        pass
    elif request.method == "POST":
        pass
    else:
        return {"response", "Request type not supported, only GET, PUT and DELETE are!"}


@app.route("/disciplinas", methods=["PUT", "DELETE", "POST"])
def disciplinas_api(path):

    if request.method == "PUT":
        pass
    elif request.method == "DELETE":
        pass
    elif request.method == "POST":
        pass
    else:
        return {"response", "Request type not supported, only GET, PUT and DELETE are!"}

if __name__ == '__main__':
    app.run()