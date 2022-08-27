#aula 12 - array in python

secreto = "computador"
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print("suas chances acabaram...")
        break

    letra = input("Digite uma letra: ")
    if len(letra) > 1:
        print("Digite apenas uma letra...")
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f"PARABENS!!!, A letra -{letra}- existe na palavra secreta")
    else:
        print(f"Continue tentando... a letra -{letra}- não existe na palavra secreta")
        digitadas.pop()

    secreto_temporario = ""
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += "*"

    if secreto_temporario == secreto:
        print(f"PARABENS, voce ganhou!!! \n esta era a palavra -{secreto_temporario}-")
        break
    else:
        print(f"A palavra secreta esta assim: -{secreto_temporario}-")

    if letra not in secreto:
        chances -= 1
    print(f"voce ainda tem {chances} chances")
    print()