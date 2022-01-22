"""
GERENCIAMENTO DE DEVS COM A EXTENSÃO RESTFUL DO FLASK
"""

from flask import Flask, request
from flask_restful import Resource, Api
from skills import Skills
import json

app = Flask(__name__)
api = Api(app)

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

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = "Desenvolvedor do ID {} nao existe".format(id)
            response = {"status":"ERROR","mensagem":mensagem}
        except Exception:
            mensagem = "Error desconhecido. Por favor, procure o administrador da API"
            response = {"status": "ERROR", "mensagem": mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        if dados["nome"]:
            desenvolvedores[id]["nome"] = dados["nome"]
        if dados["skills"]:
            desenvolvedores[id]["skills"] = dados["skills"]
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {"status":"sucesso","mensagem":"Registro excluido com sucesso"}

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        pos = len(desenvolvedores)
        dados["id"] = pos
        desenvolvedores.append(dados)
        return desenvolvedores[pos]

api.add_resource(Desenvolvedor,"/dev/<int:id>")
api.add_resource(ListaDesenvolvedores, "/dev/")
api.add_resource(Skills, "/skills/", "/skills/<int:id>")

if __name__=="__main__":
    app.run(
        debug=True
    )