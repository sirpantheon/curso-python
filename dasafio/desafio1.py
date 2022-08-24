#desafio 1 - PAR ou IMPAR

number1 = input("digite um numero INT: ")

if number1.isdigit():
    number1 = int(number1)
    if number1 % 2 == 0:
        print("Esse numero e PAR")
    else:
        print("Esse numero e IMPAR")
else:
    print("Valor Invalido")


