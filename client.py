import json
import requests

actions = ["ADD", "REMOVE", "SHOW"]
catgorias = ["ALUNO", "TURMA", ""]

categories = {"ALUNOS": "alunos",
              "TURMA": "turmas",
              "ALUNO": 'alunos',
              "DISCIPLINA": "disciplinas",
              "TURMAS": "turmas",
              "DISCIPLINAS": "disciplinas"
              }

while True:
    msg = raw_input("Comando: ")
    msg = msg.split(" ")

    if msg[0] in actions:
        try:
            if msg[1] in categories.keys():

                data = {"op": msg[0], "category": msg[1]}

                msg.pop(0)
                msg.pop(0)

                i = 0
                for index, command in enumerate(msg):
                    data[i] = msg[index]
                    i += 1

                stufff = requests.post("http://localhost:5000/" + categories[data["category"]], json=json.dumps(data))

            elif type(int(msg[0])) is int:

                data = {"op": msg[0]}
                msg.pop(0)

                requests.post("http://localhost:5000/inscricoes", json=json.dumps(data))

        except ValueError:
            print "Parametros incorrectos!"

    else:
        print "Action not supported!"
