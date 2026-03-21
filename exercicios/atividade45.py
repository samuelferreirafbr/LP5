print('Pede 5 números e verifica qual é o maior')

maior = 'nenhum'
for numero in range(5):
    valor = int(input(f'Digite o número {numero + 1}: '))
    if maior == 'nenhum' or valor > maior:
        maior = valor

print(f'O maior número digitado foi: {maior}')