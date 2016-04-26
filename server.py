import skel
import json
import sqlite3
import queries
from flask import json
from flask import Flask
from flask import request
from collections import OrderedDict


app = Flask(__name__)


def createTables():
    db.executescript(open("./database/tables.sql").read())
    conndb.commit()

DATABASE = "./database/aitd.db"

conndb = sqlite3.connect(DATABASE, check_same_thread=False)
db = conndb.cursor()
# createTables()

use = skel.Skel(conndb, db)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/alunos", methods=["POST"])
def alunos_api():

    data = json.loads(request.data, object_pairs_hook=OrderedDict)

    resp = {}

    if data["op"] == "ADD":
        filtrar = [str(data["2"]), str(data["0"]), int(data["1"])]

        db.execute(queries.add["ADD ALUNO"], filtrar)
        print db.fetchone()

        conndb.commit()
        return "OK"

    elif data["op"] == "REMOVE":
        filtrar = [int(data["0"])]

        db.execute(queries.remove["REMOVE ALUNO"], filtrar)
        print db.fetchone()

        conndb.commit()
        return "OK"

    elif data["op"] == "SHOW":
        filtrar = [int(data["0"])]

        db.execute(queries.showID["SHOW ALUNO"], filtrar)
        print db.fetchone()

        conndb.commit()
        return "OK"

    else:
        return "operation: invalid"


@app.route("/turmas", methods=["POST"])
def turmas_api():

    data = json.loads(request.data, object_pairs_hook=OrderedDict)

    if request.method == "ADD":
        filtrar = [str(data["2"]), str(data["0"]), int(data["1"])]

        db.execute(queries.add["ADD TURMA"], filtrar)
        print db.fetchone()

        conndb.commit()
        return "OK"

    elif request.method == "REMOVE":
        resp = use.turmas(data)
    elif request.method == "SHOW":
        resp = use.turmas(data)
    else:
        return {"operation": "invalid"}


@app.route("/disciplinas", methods=["POST"])
def disciplinas_api():

    data = json.loads(request.data, object_pairs_hook=OrderedDict)

    print data
    resp = "OK"

    if data["op"] == "ADD":
        filtrar = [str(data["2"]), int(data["0"]), int(data["1"])]

        print filtrar

        db.execute(queries.add["ADD DISCIPLINA"], filtrar)
        print db.fetchone()

        conndb.commit()
        return "OK"

    elif data["op"] == "REMOVE":
        resp = use.turmas(data)
    elif data["op"] == "SHOW":
        resp = use.turmas(data)
    else:
        return "OK"

    return resp


@app.route("/inscricoes", methods=["POST"])
def incricoes_api():

    data = json.loads(request.data, object_pairs_hook=OrderedDict)

    resp = {}

    if data["op"] == "ADD":
        resp = use.inscricoes(data)
    elif data["op"] == "REMOVE":
        resp = use.inscricoes(data)
    elif data["op"] == "SHOW":
        resp = use.inscricoes(data)
    else:
        return {"operation": "invalid"}

    return resp

if __name__ == '__main__':
    app.debug = True
    app.run()

# @app.route('/messages', methods=['POST'])
# def api_message():
#
#     if request.headers['Content-Type'] == 'text/plain':
#         return "Text Message: " + request.data
#
#     elif request.headers['Content-Type'] == 'application/json':
#         return "JSON Message: " + json.dumps(request.json)
#
#     elif request.headers['Content-Type'] == 'application/octet-stream':
#         f = open('./binary', 'wb')
#         f.write(request.data)
#         f.close()
#         return "Binary message written!"
#     else:
#         return "415 Unsupported Media Type ;)"
