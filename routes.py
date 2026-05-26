from flask import current_app, request, redirect, render_template
from App import app
from Tarefas import tarefas, adicionar_tarefa, completar_tarefa

@app.route('/')
def index():
    tarefas_classificadas = sorted(tarefas, key=lambda t: t['feito'])
    return render_template('index.html', tarefas=tarefas_classificadas)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    texto_tarefa = request.form.get('texto_tarefa')
    if texto_tarefa:
        adicionar_tarefa(texto_tarefa)
    return redirect('/')

@app.route('/completar/<int:id>')
def completo(id):
    completar_tarefa(id)
    return redirect('/')
