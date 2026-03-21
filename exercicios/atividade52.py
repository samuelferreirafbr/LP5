print('Solicita senha correta')

senha = input("Digite a senha: ")
while senha != '1234':
    print("Senha incorreta. Tente novamente.")
    senha = input("Digite a senha: ")
print("Senha correta")