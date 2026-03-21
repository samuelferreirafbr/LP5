print('Solicita números ao usuário até que ele digite 0 e soma os números inseridos')

soma = 0
while True:
    numero = int(input('Digite um número (ou 0 para finalizar): '))
    if numero == 0:
        break
    soma += numero

print(f'A soma dos números inseridos é: {soma}')