from flask import Flask
from flask import request
from flask import json
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

    data = json.loads(request.data, object_pairs_hook=OrderedDict)

    resp = {}

    if data["op"] == "ADD":
        resp = skel.aluno(data)
    elif data["op"] == "REMOVE":
        resp = skel.aluno(data)
    elif data["op"] == "SHOW":
        resp = skel.aluno(data)
    else:
        return {"operation": "invalid"}

    return resp


@app.route("/turmas", methods=["POST"])
def turmas_api(path):

    data = json.loads(request.data, object_pairs_hook=OrderedDict)

    resp = {}

    if request.method == "PUT":
        resp = skel.turmas(data)
    elif request.method == "DELETE":
        resp = skel.turmas(data)
    elif request.method == "POST":
        resp = skel.turmas(data)
    else:
        return {"operation": "invalid"}


@app.route("/disciplinas", methods=["PUT", "DELETE", "POST"])
def disciplinas_api(path):

    data = json.loads(request.data, object_pairs_hook=OrderedDict)

    resp = {}

    if request.method == "PUT":
        resp = skel.turmas(data)
    elif request.method == "DELETE":
        resp = skel.turmas(data)
    elif request.method == "POST":
        resp = skel.turmas(data)
    else:
        return {"operation": "invalid"}

    return resp


@app.route("/disciplinas", methods=["POST"])
def incricoes_api():

    data = json.loads(request.data, object_pairs_hook=OrderedDict)

    resp = {}

    if data["op"] == "ADD":
        resp = skel.inscricoes(data)
    elif data["op"] == "DELETE":
        resp = skel.inscricoes(data)
    elif data["op"] == "SHOW":
        resp = skel.inscricoes(data)
    else:
        return {"operation": "invalid"}

    return resp

if __name__ == '__main__':
    app.run()
