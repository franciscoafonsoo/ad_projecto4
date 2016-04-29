import json
import requests
import pprint

actions = ["ADD", "REMOVE", "SHOW"]
cat2=['ALUNOS','TURMAS','DISCIPLINAS']
categories = {"ALL ALUNOS": "alunos",
              "TURMA": "turmas",
              "ALUNO": 'alunos',
              "DISCIPLINA": "disciplinas",
              "ALL TURMAS": "turmas",
              "ALL DISCIPLINAS": "disciplinas"
              }

while True:
    msg = raw_input("Comando: ")
    msg = msg.split(" ")

    if msg[0] in actions:
        try:
            if 'ALL' in msg and msg[2] in cat2 :
                data = {"op": msg[0], "category": msg[1] + ' ' + msg[2]}
                msg.pop(0)
                msg.pop(0)
                msg.pop(0)
                i = 0
                for index, command in enumerate(msg):
                    data[i] = msg[index]
                    i += 1
                stufff = requests.post("http://localhost:5000/" + categories[data["category"]], json=json.dumps(data))
                response = json.loads(stufff.text)
                rows=response[0].keys()
                for i in rows:
                    print i + ", ",
                print " "
                for a in response:
                    for b in a.values():
                        print str(b) + ", ",
                    print " "

            elif msg[1] in categories.keys():

                data = {"op": msg[0], "category": msg[1]}

                msg.pop(0)
                msg.pop(0)

                i = 0
                for index, command in enumerate(msg):
                    data[i] = msg[index]
                    i += 1

                stufff = requests.post("http://localhost:5000/" + categories[data["category"]], json=json.dumps(data))
                response=json.loads(stufff.text)
                pprint.pprint(response)


            elif type(int(msg[1])) is int and type(int(msg[2])) is int :
                data = {"op": msg[0]}
                msg.pop(0)
                i = 0
                for index, command in enumerate(msg):
                    data[i] = msg[index]
                    i += 1
                stufff=requests.post("http://localhost:5000/inscricoes", json=json.dumps(data))
                response = json.loads(stufff.text)
                pprint.pprint(response)

        except ValueError:
            print "Parametros incorrectos!"

    else:
        print "Action not supported!"
