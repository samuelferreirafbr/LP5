print('Tabuada de um número (a tabuada vai do 1 ao 10)')

numeros = int(input('Digite um número para ver a tabuada: '))
print(f'Tabuada do {numeros}:')
for numero in range(1, 11):
    resultado = numeros * numero
    print(f'{numeros} * {numero} = {resultado}')