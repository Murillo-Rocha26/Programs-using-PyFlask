import json


tarefas = []
proximo_id = 1

def salvar_dado():
    
    with open('tarefas.json', 'w') as f:
        json.dump({'proximo_id': proximo_id, 'tarefas': tarefas}, f)

def carregar_dado():
    global proximo_id, tarefas
    try:
        with open('tarefas.json', 'r') as f:
            data = json.load(f)
            tarefas = data['tarefas']
            
            proximo_id = data['proximo_id'] 
    except FileNotFoundError:
        pass

def adicionar_tarefa(texto):
    global proximo_id
    tarefas.append({
        'id': proximo_id,
        'texto': texto,
        'feito': False
    })
    proximo_id += 1
    salvar_dado() 

def completar_tarefa(id):
    for tarefa in tarefas:
        if tarefa['id'] == id:
            tarefa['feito'] = True
            salvar_dado() 
