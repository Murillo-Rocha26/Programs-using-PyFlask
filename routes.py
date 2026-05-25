from app import app
from Tarefas import tarefas, adicionar_tarefa, completar_tarefa
from flask import request, redirect, render_template


@app.route('/')
def index():
    tarefas_classificadas = sorted(tarefas, key=lambda t: t['feito'])
    return render_template('index.html', tarefas=tarefas_classificadas)


@app.route('/adicionar', methords=['POST'])
def adicionar():
    texto_tarefa = request.form.get('texto_tarefa')
    if texto_tarefa:
        adicionar_tarefa(texto_tarefa)
    return redirect('/')


@app.route('/completar/<int:id>')
def completo(id):
    completar_tarefa(id)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
