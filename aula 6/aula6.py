#aula 6 - formatação de strings

nome = "johnatan"
sobreNome = "paixão"
idade = 27
altura = 1.70
peso = 77
maiorIdade = idade > 18
imc = peso / (altura ** 2)

print(f"imc de {nome} {sobreNome} e {imc:.2f}, \n{nome} e de maior?: {maiorIdade}")
print("----------------------------------")
print("imc de {} {} e {:.2f}, \n{} e de maior?: {}".format(nome, sobreNome, imc, nome, maiorIdade))