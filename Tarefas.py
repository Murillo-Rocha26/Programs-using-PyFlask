from app import app

tarefas = []
proximo_id = 1


def adicionar_tarefa(texto):
    global proximo_id

    tarefas.append({
        'id': proximo_id,
        'texto': texto,
        'feito': False
    })

    proximo_id += 1


def completar_tarefa(id):
    for tarefa in tarefas:
        if tarefa['id'] == id:
            tarefa['feito'] = True


if __name__ == '__main__':
    app.run(debug=True)
