import queries


class Skel:

    def __init__(self, conndb, db):
        self.data = []
        self.conndb = conndb
        self.db = db

    def addAluno(self, data):

        cometer = [(str(data["2"])), data["0"], str(data["1"])]

        self.db.execute(queries.add["ADD ALUNO"], cometer)
        print self.db.fetchone()

        self.conndb.commit()
        return "OK"

    def removeAluno(self, data):
        pass

    def showAluno(self, data):
        pass

    def inscricoes(self, data):
        print data

    def turmas(self, data):
        print data

    def disciplina(self, data):
        print data

    # def insertAluno(self, nome, nacionalidade, idade):
    #    self.db.execute("INSERT INTO alunos (nome, nacionalidade, idade) VALUES (?,?,?)", (nome, nacionalidade, idade))
    #    self.conndb.commit()
    #
    # def handler(test):
    #     request = json.loads(test)
    #     response = ''
    #     if request['cmd'] == 'ADD':
    #         insertAluno(request['nome'], request['nacionalidade'], request['idade'])
    #         response = json.dumps('OK BABY')
    #     else:
    #         response = json.dumps('NOT OK BABT')
    #     return response
