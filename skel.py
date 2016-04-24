import sqlite3
from flask import json


def createTables():
    db.executescript(open("./database/tables.sql").read())
    conndb.commit()

conndb=sqlite3.connect("./database/aitd.db")
db=conndb.cursor()
#createTables()


def insertAluno(nome,nacionalidade,idade):
    db.execute("INSERT INTO alunos (nome, nacionalidade, idade) VALUES (?,?,?)",(nome,nacionalidade,idade))
    conndb.commit()


def handler(test):
    request=json.loads(test)
    response=''
    if request['cmd']=='ADD':
        insertAluno(request['nome'],request['nacionalidade'],request['idade'])
        response=json.dumps('OK BABY')
    else:
        response=json.dumps('NOT OK BABT')
    return response


def aluno(data):
    print data


def inscricoes(data):
    print data


def turmas(data):
    print data


def disciplina(data):
    print data
