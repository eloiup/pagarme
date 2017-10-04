
# coding: utf-8

# In[1]:

import pandas as pd ## biblioteca de estruturação e analise de dados
import numpy as np ## biblioteca de algebra linear entre outras utilidades

## --------------------- ##
## plotly/dash libraries ##
## --------------------- ##

import dash
import plotly.graph_objs as go

from dash.dependencies import Input, Output, Event

import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt

from flask import Flask

## --------------------- ##

import datetime ## biblioteca para criar/trabalhar datas

#############################

## load files

vendas = pd.read_csv('UauOffice_Vendas.csv')
contratos = pd.read_csv('hubspot_Vendas.csv')

vendas['agent_id'] = vendas.id_contrato.map(lambda x: int(x[:3]))
vendas['data'] = vendas['data'].map(lambda data: pd.to_datetime(data).date())
vendas['valor'] = vendas.valor.map(lambda x: np.round(float(x),2))

agents = np.sort(contratos.id_representante.unique())


########################


server = Flask(__name__)

radio_itens = ['Todos','Selecionados']

app = dash.Dash(name = __name__, server = server, url_base_pathname='/')
app.config.supress_callback_exceptions = True

app.layout = html.Div(
    
    html.Div([
        
        html.H1(u'Dashboard Desafio Pagar.me', style={'textAlign': 'center'}),
        html.H3(u' ', style={'textAlign': 'center'}),
        html.H3(u'Data mais recente dos dados: {}'.format(datetime.datetime.today().date()), style={'textAlign': 'center'}),

    html.Div([
                html.Label('Agente', style={'fontsize':20}),
                dcc.Dropdown(
                    id = 'dropdown_agent',
                    options = [{'label':value, 'value':value} for (value) in agents],
                    multi=True,
                    ),
                dcc.RadioItems(
                    id='radio_agent',
                    options=[{'label': i, 'value': i} for i in radio_itens],
                    value=radio_itens[1],
                    ),
            ], style={'width': '20%', 'display': 'inline-block'}),
        
    html.Div([
                html.Label('Contrato', style={'fontsize':20}),
                dcc.Dropdown(
                    id = 'dropdown_contracts',
                    options = [{}],
                    multi=True,
                ),
                dcc.RadioItems(
                    id='radio_contracts',
                    options=[{'label': i, 'value': i} for i in radio_itens],
                    value=radio_itens[1],
                ),
            ], style={'width': '20%', 'display': 'inline-block'}),
        
    html.Div([
                html.Label('Grafico por', style={'fontsize':20}),
                dcc.Dropdown(
                    id = 'dropdown_graphtype',
                    options = [{'label': i, 'value': i} for i in ['Agente','Contrato']],
                    value='Agente'
                ),
                dcc.RadioItems(
                    id='radio_graphtype',
                    options=[{'label': i, 'value': i} for i in ['Acumulado','Discretizado']],
                    value='Acumulado',
                ),
            ], style={'width': '40%', 'display': 'inline-block'}),
    
    dcc.Graph(id='graph'),
        
    dt.DataTable(
        rows=[dict(zip([X for X in vendas.columns],['' for X in vendas.columns]))],

        columns=[X for X in vendas.columns],

        row_selectable=False,
        filterable=False,
        sortable=True,
        selected_row_indices=[],
        id='datatable'
    ),
        
    ],))

@app.callback(
    dash.dependencies.Output('dropdown_contracts', 'options'),
    [dash.dependencies.Input('dropdown_agent', 'value')])

def update_dropdown_agent (agents):
    
    global contratos
    
    if agents:
    
        dummy = contratos.loc[contratos.id_representante.isin(agents)]
        contracts = np.sort(dummy.id_contrato.unique())
        return [{'label':value, 'value':value} for (value) in contracts]
    
    else:
        
        return [{}]
    
@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('dropdown_agent', 'value'),dash.dependencies.Input('radio_agent', 'value'),
     dash.dependencies.Input('dropdown_contracts', 'value'),dash.dependencies.Input('radio_contracts', 'value'),
     dash.dependencies.Input('dropdown_graphtype', 'value'),dash.dependencies.Input('radio_graphtype', 'value'),])

def update_graph(dropdown_agents, radio_agents, dropdown_contracts, radio_contracts, dropdown_graphtype, radio_graphtype):
    
    global vendas
    
    vendas_copy = vendas.copy()
    
    graph_data = []
    
    d0 = pd.to_datetime('2017-01-01').date()
    df = datetime.datetime.now().date()
    
    if not dropdown_agents:
    
        if ((radio_agents == 'Selecionados') & (dropdown_graphtype == 'Agente')):
        
            return {}
    
    if not dropdown_contracts:
    
        if ((radio_contracts == 'Selecionados') & (dropdown_graphtype == 'Contrato')):
        
            return {}
    
    if dropdown_graphtype == 'Agente':
        
        if radio_agents == 'Selecionados':
            
            vendas_copy = vendas_copy.loc[vendas_copy.agent_id.isin(dropdown_agents)]
            
        for agent in np.sort(vendas_copy.agent_id.unique()):
            
            dummy_vendas = vendas_copy.loc[vendas_copy.agent_id==agent]
            
            X = []
            Y = []
            
            for date in np.arange(d0,df+datetime.timedelta(days=1)):
    
                date = pd.to_datetime(date).date() ## converte de np.datetime64 para datetime.date
            
                X.append(date)
                
                if radio_graphtype == 'Acumulado':
                    
                    value = dummy_vendas.loc[dummy_vendas['data']<=date, 'valor'].sum()
                    
                else:
                    
                    value = dummy_vendas.loc[dummy_vendas['data']==date, 'valor'].sum()
                    
                Y.append(value)
                
            if radio_graphtype == 'Acumulado':
                
                graph_data.append(go.Scatter(x=X,y=Y,mode = 'lines', name=agent))
                
            else:
                
                graph_data.append(go.Scatter(x=X,y=Y,mode = 'lines+markers', name=agent))
            
        return {'data':graph_data}
    
    else:
        
        if radio_contracts == 'Selecionados':
            
            vendas_copy = vendas_copy.loc[vendas_copy.id_contrato.isin(dropdown_contracts)]
            
        else:
            
            if radio_agents == 'Selecionados':
                
                vendas_copy = vendas_copy.loc[vendas_copy.agent_id.isin(dropdown_agents)]

        for contract in np.sort(vendas_copy.id_contrato.unique()):
            
            dummy_vendas = vendas_copy.loc[vendas_copy.id_contrato==contract]
            
            X = []
            Y = []
            
            for date in np.arange(d0,df+datetime.timedelta(days=1)):
    
                date = pd.to_datetime(date).date() ## converte de np.datetime64 para datetime.date
            
                X.append(date)
                
                if radio_graphtype == 'Acumulado':
                    
                    value = dummy_vendas.loc[dummy_vendas['data']<=date, 'valor'].sum()
                    
                else:
                    
                    value = dummy_vendas.loc[dummy_vendas['data']==date, 'valor'].sum()
                    
                Y.append(value)
                
            if radio_graphtype == 'Acumulado':
                
                graph_data.append(go.Scatter(x=X,y=Y,mode = 'lines', name=contract))
                
            else:
                
                graph_data.append(go.Scatter(x=X,y=Y,mode = 'lines+markers', name=contract))
            
        return {'data':graph_data}
    
    return {}

@app.callback(
    dash.dependencies.Output('datatable', 'rows'),
    [dash.dependencies.Input('dropdown_agent', 'value'),dash.dependencies.Input('radio_agent', 'value'),
     dash.dependencies.Input('dropdown_contracts', 'value'),dash.dependencies.Input('radio_contracts', 'value'),
     dash.dependencies.Input('dropdown_graphtype', 'value'),])

def update_datatable(dropdown_agents, radio_agents, dropdown_contracts, radio_contracts, dropdown_graphtype):

    global vendas
    
    vendas_copy = vendas.copy()
    vendas_copy = vendas_copy.sort_values(['data','agent_id'])
    
    if not dropdown_agents:
    
        if ((radio_agents == 'Selecionados') & (dropdown_graphtype == 'Agente')):
        
            return [dict(zip([X for X in vendas.columns],['' for X in vendas.columns]))]
    
    if not dropdown_contracts:
    
        if ((radio_contracts == 'Selecionados') & (dropdown_graphtype == 'Contrato')):
        
            return [dict(zip([X for X in vendas.columns],['' for X in vendas.columns]))]
        
    if dropdown_graphtype == 'Agente':
        
        if radio_agents == 'Selecionados':
            
            vendas_copy = vendas_copy.loc[vendas_copy.agent_id.isin(dropdown_agents)]
    
    else:
        
        if radio_contracts == 'Selecionados':
            
            vendas_copy = vendas_copy.loc[vendas_copy.id_contrato.isin(dropdown_contracts)]
            
        else:
            
            if radio_agents == 'Selecionados':
                
                vendas_copy = vendas_copy.loc[vendas_copy.agent_id.isin(dropdown_agents)]

    return vendas_copy.to_dict('records')
    
app.run_server(debug=False)

