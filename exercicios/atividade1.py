numeros = [1, 2, 3]

print("Números disponíveis:")
for numero in numeros:
     print(numero)

entrada = int(input('Digite números de 1 a 3: '))

if entrada == 1:
    print("Um")
elif entrada == 2:
    print("Dois")
elif entrada == 3:
    print("Três")
else:
    print("Número inválido! Digite apenas 1, 2 ou 3.")