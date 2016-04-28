import json
import sqlite3
import queries
import os.path as pa
from flask import json
from flask import Flask
from flask import request

app = Flask(__name__)
DATABASE = "./database/aitd.db"


def connect_db(dbname):
    # Existe ficheiro da base de dados?
    db_is_created = pa.isfile(dbname)

    connection = sqlite3.connect(dbname, check_same_thread=False)
    cursor = connection.cursor()
    if not db_is_created:
        cursor.executescript(open("./database/tables.sql").read())
        connection.commit()
    return connection, cursor


# receive working, missing response

# algumas queries ja implementadas e testadas. p.e ADD ALUNO (debug for now)


@app.route("/alunos", methods=["POST"])
def alunos_api():

    if request.headers['Content-Type'] == 'application/json':

        data = json.loads(request.json)
        print data

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

    else:
        return "415 Unsupported Media Type"


@app.route("/turmas", methods=["POST"])
def turmas_api():

    if request.headers['Content-Type'] == 'application/json':

        data = json.loads(request.json)

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
    else:
        return "415 Unsupported Media Type"


@app.route("/disciplinas", methods=["POST"])
def disciplinas_api():

    if request.headers['Content-Type'] == 'application/json':

        data = json.loads(request.json)

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

    else:
        return "415 Unsupported Media Type"


@app.route("/inscricoes", methods=["POST"])
def incricoes_api():

    # incompleto

    if request.headers['Content-Type'] == 'application/json':

        data = json.loads(request.json)

        if data["op"] == "ADD":
            pass
        elif data["op"] == "REMOVE":
            pass
        elif data["op"] == "SHOW":
            pass
        else:
            return {"operation": "invalid"}

        return "OK"

    else:
        return "415 Unsupported Media Type"


if __name__ == '__main__':
    conndb, db = connect_db(DATABASE)
    app.debug = True
    app.run()
