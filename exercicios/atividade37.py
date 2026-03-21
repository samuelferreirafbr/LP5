print('Verificar se o número é múltiplo de 2 ou 5:')

numero = int(input("Digite o número: "))
if numero % 2 == 0:
    print("O número é múltiplo de 2.")
elif numero % 5 == 0:
    print("O número é múltiplo de 5.")
else:
    print("O número não é múltiplo de 2 nem de 5.")