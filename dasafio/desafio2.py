#desafio 2 - que horas são
hora = input("digite a hora Atual: ")

hora = int(hora)

if hora >= 0 and hora <= 11:
    print("Bom Dia!")
elif hora > 11 and hora < 18:
    print("Boa Tarde!")
else:
    print("Boa Noite")