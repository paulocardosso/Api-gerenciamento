from flask import Flask, jsonify, redirect, url_for, request
import json

app = Flask(__name__)

tarefas = [
    {
        "id": 0,
        "responsavel":"Paulo",
        "tarefa":"Criar um site do zero",
        "status":"pendente"
    },
    {
        "id": 1,
        "responsavel":"Lorena",
        "tarefa":"Ler 10 livros",
        "status":"concluido"
    }
]

@app.route("/")
def redirecionar():
    return redirect(url_for("listartarefas"))

@app.route("/tarefas/", methods=['GET','POST'])
def listartarefas():
    if request.method == 'GET':
        return jsonify(tarefas)
    elif request.method == 'POST':
        dados = json.loads(request.data)
        ultimapos = len(tarefas)
        dados["id"] = ultimapos
        tarefas.append(dados)
        return jsonify(tarefas[ultimapos])

@app.route("/tarefas/<int:id>", methods=['GET','PUT','DELETE'])
def umatarefa(id):
    if request.method == 'GET':
        try:
            response = tarefas[id]
        except IndexError:
            msg = "Nao existe a tarefa de ID {}".format(id)
            response = {"status":"ERROR", "mensagem":msg}
        except Exception:
            msg = "Erro desconhecido!"
            response = {"status": "ERROR", "mensagem": msg}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        stts = dados["status"]
        tarefas[id]["status"] = stts
        return jsonify(tarefas[id])
    elif request.method == 'DELETE':
        tarefas.pop(id)
        msg = "A tarefa foi excluida com sucesso!"
        return jsonify({"status":"sucesso","msg":msg})

if __name__=='__main__':
    app.run(
        debug=True
    )