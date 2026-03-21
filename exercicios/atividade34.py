print('Verifica se um número é positivo, negativo ou zero')

num = float(input('Digite um número: '))
if num > 0:
    print('O número é positivo')
elif num < 0:
    print('O número é negativo')
elif num:
    print('O número é zero')
else:
    print('Entrada inválida. Por favor, digite um número válido.')