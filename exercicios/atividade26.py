print('Verificar se os dois números são múltiplos de 5 ou não:')

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
if numero1 % 5 == 0 and numero2 % 5 == 0:
    print("Os dois números são múltiplos de 5.")
else:
    print("Pelo menos um dos números não é múltiplo de 5.")