#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Aplicações distribuídas - Projeto 1 - lock_client.py
Grupo: 25
Números de aluno: 44314, 43551, 44285
"""

import datetime
year = datetime.date.today().year

add = {
    "ADD ALUNO": "INSERT INTO alunos (nacionalidade, idade, nome) VALUES (?,?,?)",
    "ADD DISCIPLINA": "INSERT INTO disciplina (ano, semestre,designacao) VALUES (?,?,?);",
    "ADD TURMA": "INSERT INTO turma (id_disciplina, tipo, designacao) VALUES (?,?,?);",
    "ADD": "INSERT INTO inscricoes (id_aluno, id_turma, ano_letivo) VALUES (?,?,?);",
}

showID = {
    "SHOW ALUNO": "SELECT * FROM alunos WHERE alunos.id=?;",
    "SHOW DISCIPLINA": "SELECT * FROM disciplina where disciplina.id=?;",
    "SHOW TURMA": "SELECT * FROM TURMA where turma.id=?;",
    "SHOW": "SELECT COUNT(*) FROM inscricoes where inscricoes.id_aluno=? and inscricoes.id_turma=?;",
}

showAllID = {
    "SHOW ALL ALUNOS TURMA": "SELECT * FROM alunos JOIN inscricoes WHERE alunos.id = inscricoes.id_aluno and inscricoes.id_turma = ?;",
    "SHOW ALL ALUNOS DISCIPLINA": "SELECT * FROM alunos join inscricoes where alunos.id = inscricoes.id_aluno and inscricoes.id_turma=(SELECT id_turma from turma where id_disciplina=?);",
    "SHOW ALL TURMAS": "SELECT id from turma where id_disciplina=?;",
}

show= {
    "SHOW ALL ALUNOS": "SELECT * FROM alunos;",
    "SHOW ALL DISCIPLINAS": "SELECT * FROM disciplina;",
    "SHOW ALL TURMAS": "SELECT * FROM turma;"
}

remove = {
    "REMOVE ALUNO": "DELETE FROM alunos where alunos.id=?;",
    "REMOVE DISCIPLINA": "DELETE FROM disciplina where disciplina.id=?;",
    "REMOVE TURMA": "DELETE FROM turma where turma.id=?;",
}

removeAll = {
    "REMOVE ALL ALUNOS": "DELETE FROM ALUNOS;",
    "REMOVE ALL DISCIPLINA": "DELETE FROM disciplina;",
    "REMOVE ALL TURMAS": "DELETE FROM turma;"
}

removeID = {
    "REMOVE ALL ALUNOS TURMA": "DELETE FROM alunos where (SELECT * FROM alunos JOIN inscricoes WHERE alunos.id = inscricoes.id_aluno and inscricoes.id_turma = ?);",
    "REMOVE ALL ALUNOS DISCIPLINAS": "DELETE FROM disciplina WHERE (SELECT * FROM alunos join inscricoes where alunos.id = inscricoes.id_aluno and inscricoes.id_turma=(SELECT id_turma from turma where id_disciplina=?));",
    "REMOVE ALL TURMAS": "DELETE FROM turma WHERE (SELECT id from turma where id_disciplina=?);",
    "REMOVE": "DELETE FROM inscricoes WHERE(SELECT * FROM inscricoes where inscricoes.id_aluno=? and inscricoes.id_turma=?);"
}


removedisciplinas = [
    "SELECT * from turma where id_disciplina = ?;",
    "DELETE FROM inscricoes WHERE id_turma = ?;",
    "DELETE FROM turma where turma.id = ?;",
    "DELETE FROM disciplina where id = ?;"
]
