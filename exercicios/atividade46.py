print('Média de 10 números')

soma = 0
for numero in range(10):
    valor = int(input(f'Digite o número {numero + 1}: '))
    soma += valor

media = soma / 10
print(f'A média dos números digitados é: {media}')