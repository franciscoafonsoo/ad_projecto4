#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_client.py
Grupo: 25
Números de aluno: 44314, 43551, 44285
"""

import sys
import json
import requests
import pprint
import urllib3

requests.packages.urllib3.disable_warnings()

actions = ["ADD", "REMOVE", "SHOW"]
cat2 = ['ALUNOS', 'TURMAS', 'DISCIPLINAS']

ano = ["1", "2", "3", "4", "5"]
semestre = ["1", "2"]
tipo = ["T", "TP", "PL", "O", "OT"]

categories = {"ALL ALUNOS": "alunos",
              "TURMA": "turmas",
              "ALUNO": 'alunos',
              "DISCIPLINA": "disciplinas",
              "ALL TURMAS": "turmas",
              "ALL DISCIPLINAS": "disciplinas"
              }


def checksingleop():
    if data["op"] == "SHOW" or data["op"] == "REMOVE":
        if msg[2].isdigit():
            return True
        else:
            print "1. parametros errados"
            return False
    else:
        return False


def checkinput():
    if data["category"] == "ALUNO":
        if msg[3].isdigit():
            return True
        else:
            print "3. parametros errados"
            return False

    if data["category"] == "DISCIPLINA":
        if msg[2] in ano and msg[3] in semestre:
            return True
        else:
            print "parametros errados"
            return False

    if data["category"] == "TURMA":
        if msg[2].isdigit() and msg[3] in tipo:
            return True
        else:
            print "4. parametros errados"
            return False


while True:
    try:
        msg = raw_input("Comando: ")
        msg = msg.split(" ")

        s = requests.session()

        if msg[0] in actions:
            try:
                if 'ALL' in msg and msg[2] in cat2:

                    data = {"op": msg[0], "category": msg[1] + ' ' + msg[2]}

                    if len(msg) > 3:
                        if msg[4].isdigit():
                            pass
                        else:
                            print "5. parametros errados"
                            continue

                    msg.pop(0)
                    msg.pop(0)
                    msg.pop(0)

                    i = 0
                    for index, command in enumerate(msg):
                        data[i] = msg[index]
                        i += 1

                    print data

                    stuff = s.post('https://localhost:5000/' + categories[data['category']], json=json.dumps(data),
                        verify='ssl/root.pem', cert=('ssl/client.crt', 'ssl/client.key'))

                    response = json.loads(stuff.text)
                    rows = response[0].keys()
                    for i in rows:
                        print i + ", ",
                    print " "
                    for a in response:
                        for b in a.values():
                            print str(b) + ", ",
                        print " "

                elif msg[1] in categories.keys():

                    data = {"op": msg[0], "category": msg[1]}

                    if checksingleop():
                        pass
                    else:
                        if checkinput():
                            pass
                        else:
                            continue

                    msg.pop(0)
                    msg.pop(0)

                    i = 0
                    for index, command in enumerate(msg):
                        data[i] = msg[index]
                        i += 1

                    print data

                    stuff = s.post('https://localhost:5000/' + categories[data['category']], json=json.dumps(data),
                        verify='ssl/root.pem', cert=('ssl/client.crt', 'ssl/client.key'))

                    response = json.loads(stuff.text)
                    pprint.pprint(response)

                elif type(int(msg[1])) is int and type(int(msg[2])) is int:

                    data = {"op": msg[0]}

                    msg.pop(0)

                    i = 0
                    for index, command in enumerate(msg):
                        data[i] = msg[index]
                        i += 1

                    print data

                    stuff = s.post("https://localhost:5000/inscricoes", json=json.dumps(data),
                        verify='ssl/root.pem', cert=('ssl/client.crt', 'ssl/client.key'))

                    response = json.loads(stuff.text)
                    pprint.pprint(response)

            except ValueError:
                print "6. parametros incorrectos"

        else:
            print "Action not supported!"
            
    except KeyboardInterrupt:
        print ""
        print "leaving..."
        sys.exit()
