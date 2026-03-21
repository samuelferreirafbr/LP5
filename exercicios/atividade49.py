print('Verifica quantos e quais dos 7 números são maiores que 10')

numeros = []
for numero in range(7):
    numeros.append(int(input(f'Digite o {numero + 1}º número: ')))

maiores_que_10 = [num for num in numeros if num > 10]
print(f'Quantidade de números maiores que 10: {len(maiores_que_10)}')
print(f'Números maiores que 10: {maiores_que_10}')