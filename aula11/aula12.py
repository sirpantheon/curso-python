#aula 11 - for in

nome = "Johnatan Sousa "
sobreNome= "Silva Paixão"
nomeAll = nome + sobreNome

for i , letra in enumerate(nomeAll):
    print(i , letra)

print("================================")

for i in range(0, 23 , 1):
    print(i)