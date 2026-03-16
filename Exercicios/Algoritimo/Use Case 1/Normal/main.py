import os
import time

nome = ""
media = float(0)
n1 = float(0)
n2 = float(0)
freq = int(0)
pres = int(0)
aulas = int(1400)


def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def sair():
    print("Saindo...")
    time.sleep(5)
    exit()


def calcular_media():
    global media
    media = (n1 + n2) / 2


def calcular_freq():
    global freq
    freq = (pres / aulas) * 100


def situacao():
    global media
    if media >= 7 and freq > 25:
        return "Aprovado"
    else:
        return "Reprovado"


def aluno():
    global nome
    global n1
    global n2
    global pres
    nome = input("Digite o nome do aluno: ")
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    pres = int(input("Digite o número de presenças: "))


if __name__ == "__main__":
    aluno()
    calcular_media()
    calcular_freq()
    print(f"Aluno: {nome}")
    print(f"Média: {media}")
    print(f"Frequência: {freq:.2f}%")
    print(f"Situação: {situacao()}")
