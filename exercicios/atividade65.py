print('Pede 5 números e mostra o maior e o menor.')

maior = 'nenhum'
menor = 'nenhum'
for numero in range(5):
    valor = int(input(f'Digite o número {numero + 1}: '))
    if maior == 'nenhum' or valor > maior:
        maior = valor
    if menor == 'nenhum' or valor < menor:
        menor = valor

print(f'O maior número digitado foi: {maior}')
print(f'O menor número digitado foi: {menor}')