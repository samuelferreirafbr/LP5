idade = int(input('Digite a idade: '))
if idade < 18:
    print("Menor de idade")
elif idade >= 18:
    print("Maior de idade")
else:
    print("Idade inválida! Digite um número inteiro positivo.")