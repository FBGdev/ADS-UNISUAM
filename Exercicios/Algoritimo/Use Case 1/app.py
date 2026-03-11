from flask import Flask, request, jsonify
import json

app = Flask(__name__)

arquivo = "alunos.json"

with open(arquivo, "r") as f:
    dados = json.load(f)

@app.route("/alunos", methods=["GET"])
def listar_alunos():
    return jsonify(dados["alunos"])

@app.route("/alunos", methods=["POST"])
def adicionar_aluno():

    novo_aluno = request.json

    dados["alunos"].append(novo_aluno)

    with open(arquivo, "w") as f:
        json.dump(dados, f, indent=4)

    return jsonify(novo_aluno)

@app.route("/alunos/<int:id>", methods=["GET"])
def buscar_aluno(id):

    for aluno in dados["alunos"]:
        if aluno["id"] == id:
            return jsonify(aluno)

    return jsonify({"erro": "Aluno não encontrado"})

@app.route("/alunos/<int:id>", methods=["DELETE"])
def del_aluno(id):
    for aluno in dados["alunos"]:
        if aluno["id"] == id:
            dados["alunos"].remove(aluno)
            with open(arquivo, "w") as f:
                json.dump(dados, f, indent=4)
            return jsonify({"mensagem": "Aluno removido com sucesso"})
    return jsonify({"erro": "Aluno não encontrado"})

@app.route("/alunos/<int:id>", methods=["PUT"])
def atualizar_aluno(id):
    for aluno in dados["alunos"]:
        if aluno["id"] == id:
            aluno_atualizado = request.json
            aluno.update(aluno_atualizado)
            with open(arquivo, "w") as f:
                json.dump(dados, f, indent=4)
            return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"})

if __name__ == "__main__":
    app.run(debug=True)