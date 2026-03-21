print('Exibe os divisores de um número')

numero = int(input('Digite um número: '))
print(f'Os divisores de {numero} são:')
for divisor in range(1, numero + 1):
    if numero % divisor == 0:
        print(divisor)