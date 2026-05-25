import json


def salvar_dado():
    with open('tarefas.json', 'w') as f:
        json.dump({'proximo_id': proximo_id, 'tarefas': 'tarefas'}, f)


def carregar_dado():
    global proximo_id, tarefas


try:
    with open('tarefas.json', 'r') as f:
        data = json.load(f)
    tarefas = data['tarefas']
    proximo_id = dado['proximo_id']


except FileNotFoundError:
    pass
