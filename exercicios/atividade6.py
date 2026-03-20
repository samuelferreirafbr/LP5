operacao = input("Escolha uma operação (+, -, *, /): ")

numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))

if operacao == '+':
    resultado = numero1 + numero2

elif operacao == '-':
    resultado = numero1 - numero2

elif operacao == '*':
    resultado = numero1 * numero2

elif operacao == '/':
    resultado = numero1 / numero2

print(f"O resultado da operação é: {resultado}")