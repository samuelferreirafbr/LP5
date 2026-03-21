print('Solicita um número e continua até inserir um número acima de 100')

while True:
    numero = int(input('Digite um número (ou acima de 100 para finalizar): '))
    if numero > 100:
        print('Número acima de 100 inserido. Finalizando o programa.')
        break