import os
from funcoes import soma, sub, menu

continuar = 's'
while continuar != 'n':

    # Vai limpar toda vez que resetar
    os.system('cls')
    opcao = menu()

    numero1 = int(input("Informe o primeiro número: "))
    numero2 = int(input("Informe o segundo número: "))

    if opcao == '1':
        soma(numero1, numero2)

    elif opcao == '2':
        sub(numero1, numero2)
    else:
        print('Opção inválida')

    continuar = input('Deseja realizar outra soma s/n? ')