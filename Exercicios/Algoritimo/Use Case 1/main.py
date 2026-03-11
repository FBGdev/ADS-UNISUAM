import time
import requests
import os

url = 'http://127.0.0.1:5000/alunos'

resposta = requests.get(url)

dados = resposta.json()

def listar_alunos():
    limpar()
    print("Lista de Alunos:\n")
    resposta = requests.get(f"{url}")
    dados = resposta.json()
    for aluno in dados:
        print(f"ID: {aluno['id']}, Nome: {aluno['nome']}, Nota 1: {aluno['n1']}, Nota 2: {aluno['n2']}, Presença: {aluno['presenca']}")

def adicionar_aluno():
    novo_aluno = input("Digite o nome do aluno: ")
    n1 = float(input("Digite a Nota 1 do aluno: "))
    n2 = float(input("Digite a Nota 2 do aluno: "))
    presenca = int(input("Digite a presença do aluno: "))
    resposta = requests.post(url, json={"nome": novo_aluno, "n1": n1, "n2": n2, "presenca": presenca})
    print(resposta.json())

def buscar_aluno():
    id_aluno = int(input("Digite o ID do aluno: "))
    resposta = requests.get(f"{url}/{id_aluno}")
    print(resposta.json())

def del_aluno():
    id_aluno = int(input("Digite o ID do aluno: "))
    resposta = requests.delete(f"{url}/{id_aluno}")
    print(resposta.json())

def atualizar_aluno():
    id_aluno = int(input("Digite o ID do aluno: "))
    novo_nome = input("Digite o novo nome do aluno: ")
    n1 = float(input("Digite a nova Nota 1 do aluno: "))
    n2 = float(input("Digite a nova Nota 2 do aluno: "))
    presenca = int(input("Digite a nova presença do aluno: "))
    resposta = requests.put(f"{url}/{id_aluno}", json={"nome": novo_nome, "n1": n1, "n2": n2, "presenca": presenca})
    print(resposta.json())

def calcular_media():
    id_aluno = int(input("Digite o ID do aluno: "))
    resposta = requests.get(f"{url}/{id_aluno}")
    aluno = resposta.json()
    if aluno:
        media = (aluno['n1'] + aluno['n2']) / 2
        print(f"A média do aluno {aluno['nome']} é: {media}")
    else:
        print("Aluno não encontrado.")

def sair():
    limpar()
    print("Saindo do programa em 5 segundos.")
    time.sleep(5)
    exit()

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def situacao_final():
    id_aluno = int(input("Digite o ID do aluno: "))
    resposta = requests.get(f"{url}/{id_aluno}")
    aluno = resposta.json()
    if aluno:
        media = (aluno['n1'] + aluno['n2']) / 2
        if media >= 7 and aluno['presenca'] >= 350:
            print(f"O aluno {aluno['nome']} está aprovado.")
        else:
            print(f"O aluno {aluno['nome']} está reprovado.")
    else:
        print("Aluno não encontrado.")

def main():
    while True:
        print("\nMenu:")
        print("1. listar alunos")
        print("2. adicionar aluno")
        print("3. buscar aluno")
        print("4. deletar aluno")
        print("5. atualizar aluno")
        print("6. calcular média")
        print("7. verificar situação final")
        print("8. sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            listar_alunos()
        elif escolha == '2':
            adicionar_aluno()
        elif escolha == '3':
            buscar_aluno()
        elif escolha == '4':
            del_aluno()
        elif escolha == '5':
            atualizar_aluno()
        elif escolha == '6':
            calcular_media()
        elif escolha == '7':
            situacao_final()
        elif escolha == '8':
            sair()
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
