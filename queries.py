import sqlite3

add = {
    "ADD ALUNO": "INSERT INTO alunos (nome, nacionalidade, idade) VALUES (?,?,?)",
    "ADD DISCIPLINA": "INSERT INTO disciplina (designacao, ano, semestre) VALUES (?,?,?);",
    "ADD TURMA": "INSERT INTO turma (id_disciplina, tipo, designacao) VALUES (?,?,?);",
    "ADD": "INSERT INTO inscricoes (id_aluno, id_turma, ano_letivo) VALUES (?,?,?);",
}

showID = {
    "SHOW ALUNO": "SELECT * FROM alunos WHERE alunos.id=?;",
    "SHOW DISCIPLINA": "SELECT * FROM disciplina where disciplina.id=?;",
    "SHOW TURMA": "SELECT * FROM TURMA where turma.id=?;",
    "SHOW": "SELECT COUNT(*) FROM inscricoes where inscricoes.id_aluno=? and inscricoes.id_turma=?;",
}

showAll = {
    "SHOW ALL ALUNOS T": "SELECT * FROM alunos JOIN inscricoes WHERE alunos.id = inscricoes.id_aluno and inscricoes.id_turma = ?;",
    "SHOW ALL ALUNOS D": "SELECT * FROM alunos join inscricoes where alunos.id = inscricoes.id_aluno and inscricoes.id_turma=(SELECT id_turma from turma where id_disciplina=?);",
    "SHOW ALL TURMAS": "SELECT id_turma from turma where id_disciplina=?;",
}

show = {
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
    "REMOVE ALL TURMA": "DELETE FROM turma;"
}

removeID = {
    "REMOVE ALL ALUNOS T": "DELETE FROM alunos where (SELECT * FROM alunos JOIN inscricoes WHERE alunos.id = inscricoes.id_aluno and inscricoes.id_turma = ?);",
    "REMOVE ALL ALUNOS D": "DELETE FROM disciplina WHERE (SELECT * FROM alunos join inscricoes where alunos.id = inscricoes.id_aluno and inscricoes.id_turma=(SELECT id_turma from turma where id_disciplina=?));",
    "REMOVE ALL TURMAS D": "DELETE FROM turma WHERE (SELECT id_turma from turma where id_disciplina=?);",
    "REMOVE": "DELETE FROM inscricoes WHERE(SELECT * FROM inscricoes where inscricoes.id_aluno=? and inscricoes.id_turma=?);"
}
