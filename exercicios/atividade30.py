print('Verificando se o usuário pode votar ou não:')

idade = int(input("Digite a idade do usuário: "))
if idade >= 16:
    print("O usuário pode votar.")
else:
    print("O usuário não pode votar.")