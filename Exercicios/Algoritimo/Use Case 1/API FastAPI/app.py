
from fastapi import FastAPI
import json
from pydantic import BaseModel

app = FastAPI()

banco = "data.json"

aulas = int(1400)

class Alunos(BaseModel):
    id: int
    nome: str
    nota1: float
    nota2: float
    presenca: int


with open(banco, "r") as f:
    data = json.load(f)

@app.get("/alunos")
def chamar_alunos():
    return data

@app.get("/alunos/{id}")
def alunos_id(id: int):
    for aluno in data:
        if int(aluno["id"]) == id:
            return aluno
        
    return {"erro": "aluno nao encontrado"}

@app.post("/alunos")
def cadastrar_alunos(aluno: dict):

    if data:
        novoId = int(data[-1]["id"]) + 1
    else:
        novoId = 1

    aluno["id"] = int(novoId)
    data.append(aluno)
    with open(banco, "w") as f:
      json.dump(data, f, indent= 4)
    
    return {"sucesso": "aluno adicionado com sucesso"}

@app.delete("/alunos/{id}")
def deletar_aluno(id: int):
    for aluno in data:
        if aluno["id"] == id:
           data.remove(aluno)
           with open(banco, "w") as f:
                json.dump(data, f, indent=4)
           return {"sucesso": "Aluno removido com Sucesso"}
    
    return {"ERRO": "erro a remover aluno"}
    
@app.put("/alunos/{id}")
def atualizar_alunos(id: int, dados: Alunos):
    for aluno in data:
        if int(aluno["id"]) == id:
            aluno["nome"] = dados.nome
            aluno["nota1"] = dados.nota1
            aluno["nota2"] = dados.nota2
            aluno["presenca"] = dados.presenca

            with open(banco, "w") as f:
                json.dump(data, f, indent=4)

            return {"sucesso": "Aluno atualizado com sucesso"}

    return {"erro": "Aluno não encontrado"}
    
@app.get("/alunos/{id}/situacao")
def situacao_aluno(id: int):
    for aluno in data:
        if int(aluno["id"]) == id:
            media = (float(aluno["nota1"]) + float(aluno["nota2"])) / 2
            presenca_percentual = (int(aluno["presenca"]) / aulas) * 100

            if presenca_percentual < 75:
                situacao = "Reprovado por Falta"
            elif media >= 7:
                situacao = "Aprovado"
            elif 4 <= media < 7:
                situacao = "Prova Final"
            else:
                situacao = "Reprovado por Nota"

            return {
                "nome": aluno["nome"],
                "media": media,
                "presenca_percentual": presenca_percentual,
                "situacao_final": situacao
            }
    return {"erro": "Aluno não encontrado"}


    

