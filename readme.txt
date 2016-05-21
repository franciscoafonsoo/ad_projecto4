Projeto de Aplicações Distribuidas do grupo 025

Francisco Pires, nº44314 Alexandre Machado nº43551 Nuno Silva, nº44285

------------------ QUARTA Entrega ------------------


Ficheiros pertencentes a entrega: server.py, client.py, queries.py e aitd.db

Comandos disponiveis no cliente: ADD ALUNO, ADD DISCIPLINA, ADD TURMA, ADD <id_aluno> <id_turma>, SHOW/REMOVE ALUNO, SHOW/REMOVE TURMA, SHOW/REMOVE ALL ALUNOS|TURMAS|DISCIPLINAS, SHOW/REMOVE <id_alunos> <id_turma>, SHOW ALUNOS TURMA, SHOW ALUNOS DISCIPLINA, SHOW TURMAS, REMOVE ALL ALUNOS DISCIPLINA, REMOVE ALL ALUNOS TURMA.

Nota:
As seguintes alterações foram feitas:
- alteração no script para gerar a BD, no qual pusemos a condição ON CASCADE DELETE. Isto porque nos facilita a vida imensamente visto que, por exemplo, ao eliminar um aluno, as inscrições que contêm esse alunos são eliminadas tambem.
- alteração aos comandos REMOVE ALL ALUNOS, em que pusemos um identificador para o id ficando: REMOVE ALL ALUNOS DISCIPLINA <id> e REMOVE ALL ALUNOS TURMA <id>
- usamos uma ligação requests.session() para fazer uma ligação persistente entre o cliente e o servidor
- ao nivel de performace, usamos a condição "threaded=True" e tentámos limitar as chamadas a BD (a implementação do CASCADE tambem permite menos chamadas à BD)

Junto dos ficheiros indicados para enviar pelos Professores, enviamos tambem o nosso ficheiro "tables.sql" visto que
modifica-mos o original dado pelos Professores.
O programa está apto para executar o ficheiro "table.sql" quando se inicia o server.py se não houver uma BD já criada.