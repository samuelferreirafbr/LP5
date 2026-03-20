transporte = input('Digite o modo de transporte (carro, bicicleta ou pe): ')
if transporte == 'carro':
    print("Velocidade média do carro: 60 km/h.")
elif transporte == 'bicicleta':
    print("Velocidade média da bicicleta: 15 km/h.")
elif transporte == 'pe':
    print("Velocidade média a pé: 5 km/h.")
else:
    print("Modo de transporte inválido! Digite carro, bicicleta ou pe.")