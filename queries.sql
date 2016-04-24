-- Inserir cenas

-- ADD ALUNO - - -
INSERT INTO alunos (nome, nacionalidade, idade) VALUES (?,?,?);
-- ADD DISCIPLINA - - -
INSERT INTO disciplina (designacao, ano, semestre) VALUES (?,?,?);
-- ADD TURMA - - -
INSERT INTO turma (id_disciplina, tipo, designacao) VALUES (?,?,?);
-- Inscrição - -
INSERT INTO inscricoes (id_aluno, id_turma, ano_letivo) VALUES (?,?,?);


-- Buscar coisas especificas
-- SHOW ALUNO
SELECT * FROM alunos WHERE alunos.id=?;
-- SHOW DISCIPLINA
SELECT * FROM disciplina where disciplina.id=?;
-- SHOW TURMA
SELECT * FROM TURMA where turma.id=?;
-- SHOW - -
SELECT COUNT(*) FROM inscricoes where inscricoes.id_aluno=? and inscricoes.id_turma=?;

--- Buscar tudo de uma tabela

--SHOW ALL ALUNOS
SELECT * FROM alunos;
--SHOW ALL DISCIPLINAS
SELECT * FROM disciplina;
-- SHOW ALL TURMAS
SELECT * FROM turma;

-- Buscar operacoes ALL --

--SHOW ALL ALUNOS -ID TURMA-
SELECT * FROM alunos JOIN "inscricoes" WHERE alunos.id = inscricoes.id_aluno and inscricoes.id_turma = ?;
--SHOW ALL ALUNOS -ID DISCIPLINA-
SELECT * FROM alunos join inscricoes where alunos.id = inscricoes.id_aluno and inscricoes.id_turma=(SELECT id_turma from turma where id_disciplina=?);
-- SHOW ALL TURMAS -ID DISCIPLINA-
SELECT id_turma from turma where id_disciplina=?;
---Apagar cenas---

--REMOVE ALUNO
DELETE FROM alunos where alunos.id=?;
--REMOVE DISCIPLINA
DELETE FROM disciplina where disciplina.id=?;
--REMOVE TURMA
DELETE FROM turma where turma.id=?;

---Apagar tudos---

DELETE FROM ALUNOS;
DELETE FROM disciplina;
DELETE FROM turma;

--Apagar todos com ids---

--REMOVE ALL ALUNOS -ID TURMA-
DELETE FROM alunos where (SELECT * FROM alunos JOIN "inscricoes" WHERE alunos.id = inscricoes.id_aluno and inscricoes.id_turma = ?);
--REMOVE ALL ALUNOS -ID DISCIPLINA-
DELETE FROM disciplina WHERE (SELECT * FROM alunos join inscricoes where alunos.id = inscricoes.id_aluno and inscricoes.id_turma=(SELECT id_turma from turma where id_disciplina=?));
--REMOVE ALL TURMAS -ID DISCIPLINA-
DELETE FROM turma WHERE (SELECT id_turma from turma where id_disciplina=?);
--REMOVE - -
DELETE FROM inscricoes WHERE(SELECT * FROM inscricoes where inscricoes.id_aluno=? and inscricoes.id_turma=?);

