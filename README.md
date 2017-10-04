# pagar.me
### case study

##### Exercicio 1

Arquivos:

random_data_generator.ipynb: 

Gera tabelas de dados para simular aquelas que seriam encontradas no banco postgresql e no Hubspot.
As tabelas sao bem simplificadas, apenas para demonstrar a aplicacao dash.

hubspot.py & postgresql.py: 

Exemplos de codigo de extração de dados do banco e aplicação.

dashboard.py:

Dashboard interativo. Hosteado localmente. Se feito numa ec2 pode-se liberar a porta para acesso por terceiros.
Output deste dash:

![alt text](https://i.imgur.com/mQ9BUcU.gif)

Resposta ao enunciado:

Subiria uma maquina ec2.
Usaria um agendador de tarefas (crontab ou jenkins) para fazer a extração de dados e update do dashboard periodicamente

Em adicao, pode-se colocar nesses serviços uma notificação por email para quando qualquer um dos scripts falhar.

Disclaimer:
Os dados gerados/plotados sao apenas para demonstracao da funcionalidade da ferramenta, e nao para uma analise aprofundada dos mesmos, uma vez que parece ser esse o intuito do exercicio.

