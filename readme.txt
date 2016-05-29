Projeto de Aplicações Distribuidas do grupo 025

Francisco Pires
Alexandre Machado
Nuno Silva

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

------------------ iptables ------------------

As regras aplicadas foram as seguintes

	ligacoes ja estabelecidas:

	sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
	sudo iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

	lookups dns:

	sudo iptables -A INPUT -p udp --sport 53 -j ACCEPT
	sudo iptables -A INPUT -p tcp --sport 53 -j ACCEPT
	sudo iptables -A OUTPUT -p udp --dport 53 -j ACCEPT
	sudo iptables -A OUTPUT -p tcp --dport 53 -j ACCEPT

	servidor recebe ligacoes dos clientes

	sudo iptables -A INPUT -p tcp --dport 5000 -j ACCEPT

	recebe pings da maquina nemo

	sudo iptables -A INPUT -d nemo.alunos.di.fc.ul.pt -p icmp -j ACCEPT

	acesso de maquinas default:


	sudo iptables -A INPUT -d "10.101.253.11, 10.101.253.12, 10.101.253.13, 10.121.53.14, 10.121.53.15, 10.101.53.16, 10.101.249.63, 10.101.85.6, 10.101.85.138, 10.101.85.18, 10.101.148.1, 10.101.85.134" -j ACCEPT
	sudo iptables -A OUTPUT -d "10.101.253.11, 10.101.253.12, 10.101.253.13, 10.121.53.14, 10.121.53.15, 10.101.53.16, 10.101.249.63, 10.101.85.6, 10.101.85.138, 10.101.85.18, 10.101.148.1, 10.101.85.134" -j ACCEPT

	loopback

	sudo iptables -A INPUT -i lo -j ACCEPT
	sudo iptables -A OUTPUT -o lo -j ACCEPT

	rejeita ligacoes restantes

	sudo iptables -A INPUT  -j DROP
	sudo iptables -A OUTPUT -j DROP

Teste iptables com o comando iptables -L

Chain INPUT (policy ACCEPT)
target     prot opt source               destination         
ACCEPT     all  --  anywhere             anywhere             state RELATED,ESTABLISHED
ACCEPT     udp  --  anywhere             anywhere             udp spt:domain
ACCEPT     tcp  --  anywhere             anywhere             tcp spt:domain
ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:5000
ACCEPT     icmp --  anywhere             nemo.alunos.di.fc.ul.pt 
ACCEPT     all  --  anywhere             10.101.253.11       
ACCEPT     all  --  anywhere             10.101.253.12       
ACCEPT     all  --  anywhere             10.101.253.13       
ACCEPT     all  --  anywhere             10.121.53.14        
ACCEPT     all  --  anywhere             10.121.53.15        
ACCEPT     all  --  anywhere             10.101.53.16        
ACCEPT     all  --  anywhere             10.101.249.63       
ACCEPT     all  --  anywhere             iate.di.fc.ul.pt    
ACCEPT     all  --  anywhere             falua.di.fc.ul.pt   
ACCEPT     all  --  anywhere             nemo.alunos.di.fc.ul.pt 
ACCEPT     all  --  anywhere             submarino.alunos.di.fc.ul.pt 
ACCEPT     all  --  anywhere             farol.alunos.di.fc.ul.pt 
ACCEPT     all  --  anywhere             anywhere            
DROP       all  --  anywhere             anywhere            

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination         
ACCEPT     all  --  anywhere             anywhere             state RELATED,ESTABLISHED
ACCEPT     udp  --  anywhere             anywhere             udp dpt:domain
ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:domain
ACCEPT     all  --  anywhere             10.101.253.11       
ACCEPT     all  --  anywhere             10.101.253.12       
ACCEPT     all  --  anywhere             10.101.253.13       
ACCEPT     all  --  anywhere             10.121.53.14        
ACCEPT     all  --  anywhere             10.121.53.15        
ACCEPT     all  --  anywhere             10.101.53.16        
ACCEPT     all  --  anywhere             10.101.249.63       
ACCEPT     all  --  anywhere             iate.alunos.di.fc.ul.pt 
ACCEPT     all  --  anywhere             falua.di.fc.ul.pt   
ACCEPT     all  --  anywhere             nemo.alunos.di.fc.ul.pt 
ACCEPT     all  --  anywhere             submarino.alunos.di.fc.ul.pt 
ACCEPT     all  --  anywhere             farol.alunos.di.fc.ul.pt 
ACCEPT     all  --  anywhere             anywhere            
DROP       all  --  anywhere             anywhere      

Testes das regras:

	servidor recebe ligacoes do cliente. usamos o python -m SimpleHTTPServer 5000 para simular o servidor visto que o python dos labs nao corre o 
	projecto

		python -m SimpleHTTPServer 5000
		10.101.148.82 - - [21/May/2016 21:06:35] code 400, message Bad request syntax ('GET')
		10.101.148.82 - - [21/May/2016 21:06:35] "GET" 400 -


	usamos depois o telnet para simular o cliente

		fc44314@DI1222-01:~$ telnet 10.101.148.83 5000
		Trying 10.101.148.83...
		Connected to 10.101.148.83.
		Escape character is '^]'.
		GET
		...
		Connection closed by foreign host.

		ping 10.101.148.82
		PING 10.101.148.82 (10.101.148.82) 56(84) bytes of data.
		ping: sendmsg: Operation not permitted
		ping: sendmsg: Operation not permitted
		ping: sendmsg: Operation not permitted

	
	para testar nemo, trocamos o ip do nemo por outra maquina do laboratorio para poder fazer ping

		ip origem do ping: 10.101.148.82
		ip para receber ping: 10.101.148.83

		ping 10.101.148.83
		PING 10.101.148.83 (10.101.148.83) 56(84) bytes of data.
		64 bytes from 10.101.148.83: icmp_seq=1 ttl=64 time=0.300 ms
		64 bytes from 10.101.148.83: icmp_seq=2 ttl=64 time=0.293 ms
		64 bytes from 10.101.148.83: icmp_seq=3 ttl=64 time=0.350 ms
		64 bytes from 10.101.148.83: icmp_seq=4 ttl=64 time=0.273 ms

------------------ snort ------------------


## obtido indo ao google fazendo pesquisas random
05/21-21:35:27.013860  [**] [1:20160521:0] port scan detected [**] [Priority: 0] {TCP} 10.121.72.23:2049 -> 10.101.148.82:748


05/21-21:35:27.013860  [**] [1:20160521:0] port scan detected [**] [Priority: 0] {TCP} 10.121.72.23:2049 -> 10.101.148.82:748
