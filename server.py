import json
import sqlite3
import queries
import os.path as po
from flask import json
from flask import Flask
from flask import request
from collections import OrderedDict


app = Flask(__name__)
DATABASE = "./database/aitd.db"


def connect_db(dbname):
    # Existe ficheiro da base de dados?
    db_is_created = po.isfile(dbname)

    connection = sqlite3.connect(dbname, check_same_thread=False)
    cursor = connection.cursor()
    if not db_is_created:
        cursor.executescript(open("./database/tables.sql").read())
        connection.commit()
    return connection, cursor


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/alunos", methods=["POST"])
def alunos_api():

    data = json.loads(request.data, object_pairs_hook=OrderedDict)

    # resp = {}

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

    if data["op"] == "ADD":
        filtrar = [str(data["2"]), str(data["0"]), int(data["1"])]

        db.execute(queries.add["ADD TURMA"], filtrar)
        print db.fetchone()

        conndb.commit()
        return "OK"

    elif data["op"] == "REMOVE":
        pass
    elif data["op"] == "SHOW":
        pass
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
        pass
    elif data["op"] == "SHOW":
        pass
    else:
        return "OK"

    return resp


@app.route("/inscricoes", methods=["POST"])
def incricoes_api():

    data = json.loads(request.data, object_pairs_hook=OrderedDict)

    resp = {}

    if data["op"] == "ADD":
        pass
    elif data["op"] == "REMOVE":
        pass
    elif data["op"] == "SHOW":
        pass
    else:
        return {"operation": "invalid"}

    return resp

if __name__ == '__main__':
    conndb, db = connect_db(DATABASE)
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
