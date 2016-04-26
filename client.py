import requests
import json
from collections import OrderedDict

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

                data = OrderedDict([("op", msg[0]), ("category", msg[1])])

                msg.pop(0)
                msg.pop(0)

                i = 0
                for index, command in enumerate(msg):
                    data[i] = msg[index]
                    i += 1

                headers = {
                }

                stuff = requests.post("http://localhost:5000/"+categories[data["category"]],
                                      data=json.dumps(data), headers=headers)

            elif type(int(msg[0])) is int:

                data = OrderedDict([("op", msg[0])])

                msg.pop(0)
                i = 0

                headers = {
                }

                requests.post("http://localhost:5000/incricoes",
                              data=json.dumps(data), headers=headers)
        except ValueError:
            print "Parametros incorrectos!"

    else:
        print "Action not supported!"

