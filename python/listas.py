# nome = 'Luciano'

# print(f'Meu nome é: {nome}')

# nome = 'Marcelo'

# print(f'Meu nome é: {nome}')



# nomes = ['Luciano', 'Marcelo', 'Samuel']

# print(nomes[0])
# print(nomes[1])
# print(nomes[2])


apostolos = ['Matheus', 'Tiago', 'Lucas', 'Judas', 'Pedro']

# percorrendo a lista posição por posição
# for apostolo in apostolos:
#     print(apostolo)

# Adicionando litem no final da lista
# print(apostolos)
# apostolos.append('João')
# print(apostolos)

# Adicionando item na posição 3
# apostolos.insert(2, 'Simão')
# print(apostolos)



# Expandindo a lista com novos elementos (+ de 1)
cavaleiros = ['Seiya', 'Shiryu']
print(cavaleiros)

cavaleiros.extend(['Ikki', 'Yoga', 'Shum'])
print(cavaleiros)

# Excluir itens de uma lista
cavaleiros.pop()
print(cavaleiros)

cavaleiros.pop(0)
print(cavaleiros)

# Excluindo por valor (vale mais alem das strings)

print(apostolos)
apostolos.remove('Judas')
print(apostolos)

alunos = ['Victor', 'Lucas', 'Gabriel', 'Lucas', 'Amanda', 'Daniel']
print(alunos)
# alunos.remove('Lucas')
# print(alunos)
for indice, aluno in enumerate(alunos):
    if aluno == 'Lucas':
        alunos.pop(indice)
print(alunos)


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares = []
pares = []

for numero in numeros:
    if numero %2 != 0:
        impares.append(numero)
    elif numero % 2 == 0:
        pares.append(numero)
print(impares)
print(pares)

# Ordem crescente
print(apostolos)
apostolos.sort()
print(apostolos)

# Ordem decrescente
apostolos.reverse()
print(apostolos)

# Zera a lista
print(cavaleiros)
cavaleiros.clear()
print(cavaleiros)

# Apaga a lista da RAM
print(pares)
del pares
print(pares)