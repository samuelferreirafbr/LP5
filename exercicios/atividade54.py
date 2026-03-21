print('Solicita um número e continua até inserir um número negativo')

while True:
    numero = int(input('Digite um número (ou um número negativo para finalizar): '))
    if numero < 0:
        print('Número negativo inserido. Finalizando o programa.')
        break