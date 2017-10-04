# coding: utf-8

import psycopg2 ## biblioteca conectora para bancos postgresql
import pandas as pd ## biblioteca de estruturação e analise de dados

'''

dados conexao, caso script fosse publico, 
as informacoes estariam num json fora da pasta compartilhada
e o script faria referencia as mesmas

'''

host = 'host_name.host_address.sa-east-1.rds.amazonaws.com'
dbname = 'dbname'
port=8080
user='username'
password='password'

'''

Imagina-se que dado a natureza do problema a tabela é de tamanho relativamente pequeno,
Logo, nao ha problemas em cada requisição se buscar pela tabela inteira, 
Caso se trata-se de uma tabela extensa, o ideal seria buscar apenas por entradas novas

'''

con = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)
cur = con.cursor()
cur.execute("""SELECT * FROM Vendas_Table""")

'''

Criamos um dataframe com os dados, a extração é feita linha a linha dentro de uma lista,
ao invez de inserirmos diretamente num dataframe, por motivos de velocidade de processamento.

'''

df_columns = [col.name for col in cur.description]
rows = cur.fetchall()

df = []

for row in rows:

    df.append(list(row))

df = pd.DataFrame(df, columns=df_columns)

cur.close()
con.close()

'''

Salvamos a saida como um arquivo csv, num caso real teriamos uma pasta de output, 
com a saida sendo salva com um nome dinamico fazendo referencia a data, 
para referencia futura no caso de corrompimento/alteracoes no banco de dados.

'''

df.to_csv('UauOffice_Vendas.csv', encoding='latin-1', index=False)