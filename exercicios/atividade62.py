print('Digitar 3 nomes e criar lista:')

nomes = []
for nome in range(3):
    nome = input('Digite um nome: ')
    nomes.append(nome)

print('Lista de nomes:')
for nome in nomes:
    print(nome)