print('Solicita 5 números inteiros e soma')

soma = 0
for numero in range(5):
    valor = int(input(f'Digite o número {numero + 1}: '))
    soma += valor
print(f'A soma dos números é: {soma}')