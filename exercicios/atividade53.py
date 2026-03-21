print('Informa um número inteiro positivo e roda do número informado até 1 de forma decrescente')

numeros = int(input('Digite um número inteiro positivo: '))
if numeros > 0:
    for numero in range(numeros, 0, -1):
        print(numero)
else:
    print('Número inválido. Por favor, digite um número inteiro positivo.')