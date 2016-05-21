#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 4 - servidor flask
Grupo: 25
Números de aluno: 44314, 43551, 44285
"""

import ssl
import json
import sqlite3
import queries
import datetime
import os.path as pa
from flask import json, Flask, request, jsonify


year = datetime.date.today().year
DATABASE = "database/aitd.bd"
app = Flask(__name__)

# ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
ctx.verify_mode = ssl.CERT_REQUIRED
ctx.load_cert_chain('ssl/server.crt', 'ssl/server.key')
ctx.load_verify_locations(cafile='ssl/root.pem')


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
        cursor.executescript(open("database/tables.sql").read())
        connection.commit()
    return connection, cursor


@app.route("/alunos", methods=["POST"])
def alunos_api():

    if request.headers['Content-Type'] == 'application/json':

        data = json.loads(request.json)
        print
        print data

        query = str(data["op"] + " " + data["category"])

        if data["op"] == "ADD":
            filtrar = [str(data["0"]), str(data["1"]), str(data["2"])]
            db.execute(queries.add[query], filtrar)
            # print db.fetchone()
            conndb.commit()
            return json.dumps("OK")
        elif data["op"] == "REMOVE":

            # if data["0"] == "DISCIPLINA":
            #     queryall = "SHOW ALL ALUNOS DISCIPLINA"
            # elif data["0"] == "TURMA":
            #     queryall = "SHOW ALL ALUNOS TURMA"

            filtrar = [int(data["0"])]

            db.execute(queries.remove["REMOVE ALUNO INSCRICOES"], filtrar)
            db.execute(queries.remove[query], filtrar)

            # db.execute(queries.inscricoes[queryall], filtrar)
            # db.execute(queries.remove[queryall], filtrar)
            # print db.fetchone()
            conndb.commit()
            return json.dumps("OK")

        elif data["op"] == "SHOW":
            cai = True
            filtrar = []
            if "ALL" in data["category"].split(" ") and data.has_key("1"):
                queryDic = queries.showAllID
                query = query + " " + data["0"]
                filtrar = [int(data["1"])]
                cai = False
            else:
                queryDic = queries.showID
            try:
                filtrar = [int(data["0"])]
            except:
                if cai:
                    queryDic = queries.show
            c = db.execute(queryDic[query], filtrar)
            rquery = c.fetchall()
            # print rquery
            return json.dumps(rquery)

        else:
            resp = jsonify(resposta="Verificar Pedidos")
            resp.status_code = 400
            return resp

            # json.dumps("operation: invalid")

    else:
        resp = jsonify(resposta="Verificar Pedidos")
        resp.status_code = 400
        return resp


@app.route("/turmas", methods=["POST"])
def turmas_api():

    if request.headers['Content-Type'] == 'application/json':

        data = json.loads(request.json)
        print
        print data

        query = str(data["op"] + " " + data["category"])

        if data["op"] == "ADD":
            filtrar = [str(data["0"]), str(data["1"]), str(data["2"])]
            db.execute(queries.add[query], filtrar)
            # print db.fetchone()
            conndb.commit()
            return json.dumps("OK")
        elif data["op"] == "REMOVE":

            filtrar = [int(data["0"])]

            db.execute(queries.removeInscricaoForeignId["REMOVE TURMA INSCRICOES"], filtrar)
            db.execute(queries.remove[query], filtrar)
            # db.execute(queries.inscricoes["REMOVE ALUNO"], filtrar)
            conndb.commit()
            return json.dumps("OK")

        elif data["op"] == "SHOW":

            filtrar = []

            if "ALL" in data["category"].split(" ") and data.has_key("0"):
                queryDic = queries.showAllID
            else:
                queryDic = queries.showID
            try:
                filtrar = [int(data["0"])]
            except:
                queryDic = queries.show
            c = db.execute(queryDic[query], filtrar)
            rquery = c.fetchall()
            # print rquery
            return json.dumps(rquery)


        else:
            resp = jsonify(resposta="Verificar Pedidos")
            resp.status_code = 400
            return resp

    else:
        resp = jsonify(resposta="Verificar Pedidos")
        resp.status_code = 400
        return resp


@app.route("/disciplinas", methods=["POST"])
def disciplinas_api():

    if request.headers['Content-Type'] == 'application/json':

        data = json.loads(request.json)
        print
        print data

        query = str(data["op"] + " " + data["category"])

        if data["op"] == "ADD":
            filtrar = [str(data["0"]), str(data["1"]), str(data["2"])]
            db.execute(queries.add[query], filtrar)
            # print db.fetchone()
            conndb.commit()
            return json.dumps("OK")
        elif data["op"] == "REMOVE":

            filtrar = [int(data["0"])]
            db.execute(queries.removedisciplinas[0], filtrar)
            temp1 = db.fetchall()
            for turma in temp1:
                db.execute(queries.removedisciplinas[1], [turma["id"]])
                db.execute(queries.removedisciplinas[2], [turma["id"]])
            db.execute(queries.removedisciplinas[3], [filtrar[0]])
            conndb.commit()

            # db.execute(queries.inscricoes["REMOVE ALUNO"], filtrar)
            # db.execute(queries.remove[query], filtrar)
            # print db.fetchone()
            # conndb.commit()

            return json.dumps("OK")

        elif data["op"] == "SHOW":
            filtrar = []
            if "ALL" in data["category"].split(" ") and data.has_key("0"):
                queryDic = queries.showAllID
            else:
                queryDic = queries.showID
            try:
                filtrar = [int(data["0"])]
            except:
                queryDic = queries.show
            c = db.execute(queryDic[query], filtrar)
            rquery = c.fetchall()
            # print rquery
            return json.dumps(rquery)

        else:
            resp = jsonify(resposta="Verificar Pedidos")
            resp.status_code = 400
            return resp

    else:
        resp = jsonify(resposta="Verificar Pedidos")
        resp.status_code = 400
        return resp


@app.route("/inscricoes", methods=["POST"])
def incricoes_api():

    if request.headers['Content-Type'] == 'application/json':

        data = json.loads(request.json)
        print
        print data

        try:
            query = str(data["op"])

            print "test"

            filtrar = [str(data["0"]), str(data["1"])]

            if data["op"] == "ADD":
                fquery = queries.add[query]
                filtrar.append(year)
                resp = 'OK'
            elif data["op"] == "REMOVE":
                fquery = queries.removeID[query]
                resp = 'OK'
            elif data["op"] == "SHOW":
                fquery = queries.showID[query]
                db.execute(fquery, filtrar)
                if bool(db.fetchone()['COUNT(*)']):
                    resp = 'Esta Inscrito'
                else:
                    resp = 'Nao esta inscrito'
            db.execute(fquery, filtrar)
            print db.fetchone()
            conndb.commit()
            return json.dumps(resp)
        except:
            resp = jsonify(resposta="NOK")
            resp.status_code = 400
            return resp


if __name__ == '__main__':
    conndb, db = connect_db(DATABASE)
    app.debug = True
    # app.run(threaded = True, ssl_context = ('ssl/server.crt', 'ssl/server.key'))
    app.run(threaded=True, ssl_context=ctx)
