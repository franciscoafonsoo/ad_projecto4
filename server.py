import json
import sqlite3

from flask.helpers import make_response

import queries
import os.path as pa
from flask import json
from flask import Flask
from flask import request
import datetime
year = datetime.date.today().year
app = Flask(__name__)
DATABASE = "./database/aitd.db"

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def connect_db(dbname):
    # Existe ficheiro da base de dados?
    db_is_created = pa.isfile(dbname)

    connection = sqlite3.connect(dbname, check_same_thread=False)
    connection.row_factory = dict_factory
    cursor = connection.cursor()
    if not db_is_created:
        cursor.executescript(open("./database/tables.sql").read())
        connection.commit()
    return connection, cursor



# receive working, missing response

# algumas queries ja implementadas e testadas. p.e ADD ALUNO (debug for now)
def handlerTemp():
    if request.headers['Content-Type'] == 'application/json':

        data = json.loads(request.json)
        print data

        if not data.has_key("category"):
            try:
                query = str(data["op"])
                print "test"
                filtrar = [str(data["0"]), str(data["1"])]
                if data["op"] == "ADD":
                    fquery=queries.add[query]
                    filtrar.append(year)
                    resp='OK'
                elif data["op"] == "REMOVE":
                    fquery = queries.removeID[query]
                    resp = 'OK'
                elif data["op"] == "SHOW":
                    fquery = queries.showID[query]
                    db.execute(fquery, filtrar)
                    if(bool(db.fetchone()['COUNT(*)'])):
                        resp='Esta Inscrito'
                    else:
                        resp='Nao esta inscrito'
                db.execute(fquery, filtrar)
                print db.fetchone()
                conndb.commit()
                return json.dumps(resp)
            except:
                return json.dumps("NOK")

        else:
            query = str(data["op"] + " " + data["category"])

        if data["op"] == "ADD":
            filtrar = [str(data["0"]), str(data["1"]), str(data["2"])]
            db.execute(queries.add[query], filtrar)
            print db.fetchone()
            conndb.commit()
            return json.dumps("OK")
        elif data["op"] == "REMOVE":

            filtrar = [int(data["0"])]
            db.execute(queries.remove["REMOVE ALUNO"], filtrar)
            print db.fetchone()
            conndb.commit()
            return json.dumps("OK")

        elif data["op"] == "SHOW":
            filtrar = []
            if "ALL" in data["category"].split(" ") and data.has_key("0"):
                queryDic=queries.showAllID
            else:
                queryDic=queries.showID
            try:
                filtrar = [int(data["0"])]
            except:
                queryDic=queries.show
            c = db.execute(queryDic[query], filtrar)
            rquery = c.fetchall()
            print rquery
            return json.dumps(rquery)

        else:
            return json.dumps("operation: invalid")

    else:
        return "415 Unsupported Media Type"


@app.route("/alunos", methods=["POST"])
def alunos_api():
    return handlerTemp()

@app.route("/turmas", methods=["POST"])
def turmas_api():
    return handlerTemp()

@app.route("/disciplinas", methods=["POST"])
def disciplinas_api():
 return handlerTemp()

@app.route("/inscricoes", methods=["POST"])
def incricoes_api():
    return handlerTemp()


if __name__ == '__main__':
    conndb, db = connect_db(DATABASE)
    app.debug = True
    app.run()
