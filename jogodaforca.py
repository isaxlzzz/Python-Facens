palavra = "linguagem"

letras_usadas = []

chances = 3

print('-=' * 20)
print("            JOGO DA FORCA")
print('-=' * 20)

palavra = input("Digite a palavra secreta:")
for x in range(10):
    print()
digitadas = []
acertos = []
erros = 0
while True:
    palavradigitada = ""
    for letra in palavra:
        palavradigitada += letra if letra in acertos else "_"
    print(palavradigitada)
    if palavradigitada == palavra:
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra: ")
    if tentativa in digitadas:
        print("Erro! Você já tentou essa letra.")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    print("X==:==\nX  :   ")
    print("X  O   " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = "  |   "
    elif erros == 3:
        linha2 = " \|   "
    elif erros >= 4:
        linha2 = " \|/ "
    print("X%s" % linha2)
    linha3 = ""
    if erros == 5:
        linha3 += " /     "
    elif erros >= 6:
        linha3 += " / \ "
    print("X%s" % linha3)
    print("X\n===========")
    if erros == 6:
        print("Enforcado!")
        break
