#aula 9 - len(quantidade de char)

CPF = input("Digite seu CPF, somente os numeros por favor...")
qtdChar = len(CPF)

if qtdChar == 11 :
    print(f"CPF coletado com Sucesso!!! \n CPF: {CPF}")
else:
    print("OPS!! Algo de errado ocorreu na validação  do seu cpf")