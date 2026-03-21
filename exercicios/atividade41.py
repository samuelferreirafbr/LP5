print('Informa um número inteiro positivo e roda de 1 até o número informado')

numeros = int(input('Digite um número inteiro positivo: '))
if numeros > 0:
    for numero in range(1, numeros + 1):
        print(numero)
else:
    print('Número inválido. Por favor, digite um número inteiro positivo.')