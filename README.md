# pagar.me
### case study

(desculpa isso aqui ta em python 3)

##### Exercicio 1

Arquivos:
<br><br>
random_data_generator.ipynb: 

Gera tabelas de dados para simular aquelas que seriam encontradas no banco postgresql e no Hubspot.
As tabelas sao bem simplificadas, apenas para demonstrar a aplicacao dash.
<br><br>
hubspot.py & postgresql.py: 

Exemplos de codigo de extração de dados do banco e aplicação.
<br><br>
dashboard.py:

Dashboard interativo. Hosteado localmente. Se feito numa ec2 pode-se liberar a porta para acesso por terceiros.
Output do dash:

Filtros de agentes / contratos
Filtros de vendas acumuladas / diarias
Grafico
Tabela das vendas filtradas/contidas no grafico

Demo:<br>

![alt text](https://i.imgur.com/mQ9BUcU.gif)
<br>
Resposta ao enunciado:

Subiria uma maquina ec2.
Usaria um agendador de tarefas (crontab ou jenkins) para fazer a extração de dados e update do dashboard periodicamente

Em adicao, pode-se colocar nesses serviços uma notificação por email para quando qualquer um dos scripts falhar.
<br><br>
Disclaimer:
Os dados gerados/plotados sao apenas para demonstracao da funcionalidade da ferramenta, e nao para uma analise aprofundada dos mesmos, uma vez que parece ser esse o intuito do exercicio.

##### Exercicio 2

Como pode ser visto nos screen shoots, a base de dados do Looker nao contem os dados na de Poliomielite em 1946 na granularidade cidade, apenas por estado.

Os cinco estados com maiores numeros de contaminacao são:

Illinois 2085 <br>
Minnesota 1827 <br>
California 1596 <br>
New York 1507 <br>
Missouri 970 <br>

Vale notar que a lista de estados do Looker para essa query nao contem nem o Alaska nem o Hawai (ambos viraram estados americanos apenas em 1959)

Os estados que tiveram mais casos de Poliomielite por habitante foram: 
(com base em https://en.wikipedia.org/wiki/List_of_U.S._states_by_historical_population decada de 40)

Minnesota 6.5 a cada 10 mil  (2º em numero absoluto de casos) <br>
Colorado 5.8 a cada 10 mil   (10º em numero absoluto de casos) <br>
North Dakota 5.1 a cada 10 mil   (21º em numero absoluto de casos) <br>
Kansas 4.7 a cada 10 mil    (8º em numero absoluto de casos) <br>
Nebraska 3.9 a cada 10 mil    (13º em numero absoluto de casos) <br>

##### Exercicio 3

Aparentemente a plataforma tem a capacidade de ser conectada a banco de dados, facilitando a construcao de queries e visualizacao de dados (construção de dashboards).

A pagina https://looker.com/solutions/sales-analytics contem um video mostrando as features basicas, como a construção de funis de conversão, listagem vendas, evolução temporal, etc..

A plataforma coloca como diferencial sua capacidade de satisfazer as interações com usuarios de perfil tecnico e não tecnico simultaneamente.

Respondendo a pergunta, o Looker poderia ser conectado aos bancos, facilitando Queries, Data Visualization & Analysis, notificações por email, entre outras funcionalidades.
