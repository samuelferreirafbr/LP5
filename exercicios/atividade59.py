print('Solicita dois números e informa se o primeiro número é maior que o segundo número')

while True:
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o segundo número: '))
    
    if numero1 > numero2:
        print(f"O primeiro número '{numero1}' é maior que o segundo número '{numero2}'.")
        break
    else:
        print(f"O primeiro número '{numero1}' não é maior que o segundo número '{numero2}'. Tente novamente.")