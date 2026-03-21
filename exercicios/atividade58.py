print('Digitar a palavra "sair" para finalizar o programa')

palavra = 'sair'
while True:
    entrada = input('Digite a palavra (ou "sair" para finalizar): ')
    if entrada == palavra:
        print('Você escolheu sair. Finalizando o programa.')
        break
    else:
        print('Tente novamente!')