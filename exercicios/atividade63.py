numeros = []
for numero in range(5):
    numero = input('Digite um número: ')
    numeros.append(numero)

print('Lista de números:')
for numero in numeros:
    print(numero)

soma = 0
for numero in numeros:
    soma += int(numero)
print(f'Soma dos números: {soma}')