"""
GERENCIAMENTO DE DEVS COM O FLASK SEM RESTFUL
"""

from flask import Flask, jsonify, redirect, url_for, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
        "id": 0,
        "nome":"Paulo",
        "skills":["Python", "Django", "Flask"]
    },
    {
        "id": 1,
        "nome":"Lorena",
        "skills":["Java", "JavaScript", "HTML", "CSS"]
    },
    {
        "id": 2,
        "nome":"Ana Paula",
        "skills":["Canvas", "CSS"]
    }
]

@app.route("/")
def redirecionar():
    #return redirect(url_for("dev", id=0)) => Passando o nome da função (dev) e o parametro da função chamada (id=0)
    return redirect(url_for("listadevs")) #Passando apenas o nome da função

@app.route("/dev/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def dev(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = "Desenvolvedor do ID {} não existe".format(id)
            response = {"status":"ERROR","mensagem":mensagem}
        except Exception:
            mensagem = "Error desconhecido. Por favor, procure o administrador da API"
            response = {"status": "ERROR", "mensagem": mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({"status":"sucesso","mensagem":"Registro excluido"})

@app.route("/dev/", methods=['GET','POST'])
def listadevs():
    if request.method == 'POST':
        dados = json.loads(request.data)
        ultimpos = len(desenvolvedores)
        dados["id"] = ultimpos
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[ultimpos])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__=='__main__':
    app.run(
        debug=True
    )
