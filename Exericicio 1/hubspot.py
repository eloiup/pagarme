# coding: utf-8

## "The urllib module defines functions and classes which help in opening URLs"

try:
    import urllib2 ## se python 2 
except:
    import urllib3 ## se python 3
    
import json ## biblioteca basica para leitura/parseamento de arquivos JSON

import pandas as pd ## biblioteca de estruturação e analise de dados

'''

dados conexao, caso script fosse publico, 
as informacoes estariam num json fora da pasta compartilhada
e o script faria referencia as mesmas

'''

APIKEY_VALUE = '####-####-####-#########'
APIKEY = '?hapikey=' + APIKEY_VALUE
HS_API_URL = 'https://api.hubapi.com/..../..../..../.../....'

url = HS_API_URL + APIKEY 

response = urllib2.urlopen(url).read()

data = json.loads(response)

df = pd.io.json.json_normalize(data)

'''

Salvamos a saida como um arquivo csv, num caso real teriamos uma pasta de output, 
com a saida sendo salva com um nome dinamico fazendo referencia a data, 
para referencia futura no caso de corrompimento/alteracoes no banco de dados.

'''

df.to_csv('hubspot_Vendas.csv', encoding='latin-1', index=False)

'''
disclaimer:

nunca usei API do hubspot, nao criei um usuario/dataset 
exemplo para testa-la, pode haver erros na hora de executar esse script

'''