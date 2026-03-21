print('Crie um programa que peça ao usuário para adivinhar um número secreto entre 1 e 10. Continue pedindo até que ele adivinhe o número corretamente')

numero_secreto = 8
while True:
    numero = int(input('Digite seu palpite (entre 1 e 10): '))
    if numero == numero_secreto:
        print('Parabéns! Você adivinhou o número secreto!')
        break
    else:
        print('Tente novamente!')