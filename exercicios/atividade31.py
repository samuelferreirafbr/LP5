print('Verifica se um número de 1 a 5 é igual a 3')

num = int(input('Digite um número de 1 a 5: '))
if num == 3:    
    print('O número é igual a 3')
elif num < 1 or num > 5:
    print('Número inválido. Digite um número de 1 a 5.')
else:
    print('O número é diferente de 3')
