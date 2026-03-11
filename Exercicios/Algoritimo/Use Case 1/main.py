import json
from urllib import request

with open("db.json") as f:
    data = json.load(f)

aluno = data["alunos"][0]

from os import wait


name = request.get("name")
n1 = request.get("n1")
n2 = request.get("n2")
aulas = 1.400
pres = request.get("presenca")
media = None


def situacao_final():
    if media >= 7:
        print("voce esta aprovado")
    elif media > 4 or media < 7:
        print("voce esta de prova final")
    else:
        print("voce esta reprovado por nota")


def presenca():
    if pres >= aulas * 0.25:
        print("voce tem a frequencia necessaria")
    else:
        print("voce reprovou por faltas")


def calcular_media(n1, n2):
    return (n1 + n2) / 2


media = calcular_media(n1, n2)


def finalizar_programa():
    print("Programa sera finalizado em 3 segundos.")
    wait(3)
    exit()


def menu():
    print("1. Calcular média")
    print("2. Verificar presença")
    print("3. Verificar situação final")
    print("4. Sair")

def login():
    name = input("Digite seu nome: ")
    name = name.strip()
    if name 



def main():
    global name, n1, n2, pres
    name = aluno["nome"]
    n1 = aluno["n1"]
    n2 = aluno["n2"]
    pres = aluno["presenca"]
    media = calcular_media(n1, n2)
    situacao_final()
    presenca()
    finalizar_programa()


if __name__ == "__main__":
    main()
