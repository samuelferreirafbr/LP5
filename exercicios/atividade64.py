print("Exibe apenas os números múltiplos de 3.")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Números múltiplos de 3:")
for numero in numeros:
    if numero % 3 == 0:
        print(numero)