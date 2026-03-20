print('Meses de 1 a 12 e sua estação do ano:')

meses = int(input('Digite o número do mês: '))
if meses == 12 or meses == 1 or meses == 2:
    print("Estação do ano: Verão")
elif meses >= 3 and meses <= 5:
    print("Estação do ano: Outono")
elif meses >= 6 and meses <= 8:
    print("Estação do ano: Inverno")
elif meses >= 9 and meses <= 11:
    print("Estação do ano: Primavera")
else:
    print("Mês inválido! Digite um número de 1 a 12.")