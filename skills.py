from flask import request
from flask_restful import Resource
import json

skills = ["Python","Java","C","C++","PHP"]

class Skills(Resource):
    def get(self):
        return skills

    def put(self, id):
        dados = json.loads(request.data)
        if skills[id] == dados:
            stts = "ERROR"
            msg = "A alteracao nao foi realizada, pois os nomes das habilidades sao os mesmos"
        else:
            stts = "SUCESSO"
            msg = "A habilidade {} foi alterada para {}!".format(skills[id], dados)
            skills[id] = dados
        return {"status":stts, "mensagem":msg}

    def delete(self, id):
        stts = "SUCESSO"
        msg = "A habilidade {} foi removida com sucesso!".format(skills[id])
        skills.pop(id)
        return {"status":stts, "mensagem":msg}

    def post(self):
        dados = json.loads(request.data)
        if dados in skills:
            stts = "ERROR"
            msg = "Habilidade ja existe na lista"
        else:
            skills.append(dados)
            stts = "SUCESSO"
            msg = "A habilidade {} foi adicionada na lista".format(dados)
        return {"status": stts, "mensagem": msg}