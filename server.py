from flask import Flask
from flask import request
from flask import json
import sqlite3

def createTables():
    db.executescript(open("./database/tables.sql").read())
    conndb.commit()

conndb=sqlite3.connect("./database/aitd.db")
db=conndb.cursor()
#createTables()

def insertAluno(nome,nacionalidade,idade):
    db.execute("INSERT INTO alunos (nome, nacionalidade, idade) VALUES (?,?,?)",(nome,nacionalidade,idade))
    conndb.commit()

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


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


if __name__ == '__main__':
    app.run()