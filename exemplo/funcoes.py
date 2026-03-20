# Função = def
def soma (numero1, numero2):
    """
        Esta função recebe dois números inteiros e realiza a soma dos mesmos.
    """
    soma = numero1 + numero2
    print(f'O resultado da sua soma é: {soma}')

def sub (numero1, numero2):
    """
        Esta função recebe dois números inteiros e realiza a subtração dos mesmos.
    """
    sub = numero1 - numero2
    print(f'O resultado da sua subtração é: {sub}')

def menu():
    """
        Menu descrevendo o que o usuário pode fazer
    """
    print('1 - Somar')
    print('2 - Subtrair')
    opcao = input('O que deseja realizar? ')

    return opcao