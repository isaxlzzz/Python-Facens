import random


def instructions():
    print("Bem vindo ao jogo de adivinhação de números!")
    print("\nVocê tem 4 tentativas para acertar um número entre 1-10")
    print("\nBoa sorte mesmo que seja tudo aleatório.")


instructions()
adivinhar_limite = 1
num = random.randint(1, 10)
usuario = int(input("\nTente um número: "))

while usuario != num:

    if usuario > num:
        print("Adivinhe um número mais baixo.")

    elif usuario < num:
        print("Adivinhe um número mais alto.")

    usuario = int(input("\nTente um número: "))
    adivinhar_limite += 1

    if adivinhar_limite == 4:
        print("------------------------------------------------------")
        print("Acabou suas tentativas :( a resposta era:", num, "<--")
        print("------------------------------------------------------")
        break
else:
    print("Você acertou! a resposta era:", num,
          "e você acertou com apenas", adivinhar_limite, "tentativas")
