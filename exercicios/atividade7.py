entrada = float(input('Digite a nota (0 a 10): '))
if entrada >= 8 and entrada <= 10:
    print("Nota alta")
elif entrada >= 5 and entrada < 8:
    print("Nota média")
elif entrada >= 0 and entrada < 5:
    print("Nota baixa")
else:
    print("Nota inválida! Digite um número entre 0 e 10.")