print('Pede 10 números e exibe apenas os números pares')

pares = []

for numero in range(10):
    valor = int(input(f'Digite o número {numero + 1}: '))
    if valor % 2 == 0:
        pares.append(valor)

print('Os números pares digitados foram:')
for par in pares:
    print(par)