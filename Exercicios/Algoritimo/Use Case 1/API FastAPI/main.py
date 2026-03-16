import requests
import os
import time

api = "http://127.0.0.1:8000/alunos"
aulas = 1400

def limpar():
    os.system("cls")

def calcular_situacao(aluno):
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

    return media, presenca_percentual, situacao

def listar_alunos():
    limpar()
    resposta = requests.get(api)
    alunos = resposta.json()
    for aluno in alunos:
        media, presenca, situacao = calcular_situacao(aluno)
        print("-----------------------------")
        print(f"ID: {aluno['id']}, Nome: {aluno['nome']}, Nota1: {aluno['nota1']}, Nota2: {aluno['nota2']}, Presença: {aluno['presenca']}")
        print(f"Média: {media:.2f}, Presença: {presenca:.2f}%, Situação: {situacao}")
        print("-----------------------------\n")
    voltar = int(input("Digite 1 para Voltar ao menu:"))
    if voltar == 1:
        limpar()
        menu()
    else:
        limpar()
        print("Inválido\n")
        print("Espere 5 Segundos")
        time.sleep(5)
        listar_alunos()



    


def buscar_aluno():
    limpar()
    id = input("Digite o ID do aluno: ")
    resposta = requests.get(f"{api}/{id}")
    aluno = resposta.json()
    if "erro" in aluno:
        print(aluno["erro"])
    else:
        media, presenca, situacao = calcular_situacao(aluno)
        print("-----------------------------")
        print(f"ID: {aluno['id']}, Nome: {aluno['nome']}, Nota1: {aluno['nota1']}, Nota2: {aluno['nota2']}, Presença: {aluno['presenca']}")
        print(f"Média: {media:.2f}, Presença: {presenca:.2f}%, Situação: {situacao}")
        print("-----------------------------")
    voltar = int(input("Digite 1 para Voltar ao menu:"))
    if voltar == 1:
        limpar()
        menu()
    else:
        limpar()
        print("Inválido\n")
        print("Espere 5 Segundos")
        time.sleep(5)
        buscar_aluno()

def cadastrar_aluno():
    limpar()
    nome = input("Nome: ")
    nota1 = float(input("Nota1: "))
    nota2 = float(input("Nota2: "))
    presenca = int(input("Presença: "))
    aluno = {"nome": nome, "nota1": nota1, "nota2": nota2, "presenca": presenca}
    resposta = requests.post(api, json=aluno)
    print(resposta.json())
    voltar = int(input("Digite 1 para Voltar ao menu:"))
    if voltar == 1:
        limpar()
        menu()
    else:
        limpar()
        print("Inválido\n")
        print("Espere 5 Segundos")
        time.sleep(5)
        cadastrar_aluno()

def atualizar_aluno():
    limpar()
    id = input("ID do aluno que deseja atualizar: ")
    nome = input("Novo nome: ")
    nota1 = float(input("Nova nota1: "))
    nota2 = float(input("Nova nota2: "))
    presenca = int(input("Nova presença: "))
    aluno = {"id": int(id), "nome": nome, "nota1": nota1, "nota2": nota2, "presenca": presenca}
    resposta = requests.put(f"{api}/{id}", json=aluno)
    print(resposta.json())
    voltar = int(input("Digite 1 para Voltar ao menu:"))
    if voltar == 1:
        limpar()
        menu()
    else:
        limpar()
        print("Inválido\n")
        print("Espere 5 Segundos")
        time.sleep(5)
        atualizar_aluno()

def deletar_aluno():
    limpar()
    id = input("ID do aluno que deseja deletar: ")
    resposta = requests.delete(f"{api}/{id}")
    print(resposta.json())
    voltar = int(input("Digite 1 para Voltar ao menu:"))
    if voltar == 1:
        limpar()
        menu()
    else:
        limpar()
        print("Inválido\n")
        print("Espere 5 Segundos")
        time.sleep(5)
        deletar_aluno()

def menu():
    while True:
        print("\n1. Listar alunos")
        print("2. Buscar aluno por ID")
        print("3. Cadastrar aluno")
        print("4. Atualizar aluno")
        print("5. Deletar aluno")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_alunos()
        elif opcao == "2":
            buscar_aluno()
        elif opcao == "3":
            cadastrar_aluno()
        elif opcao == "4":
            atualizar_aluno()
        elif opcao == "5":
            deletar_aluno()
        elif opcao == "6":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()