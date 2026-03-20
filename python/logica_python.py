# Criando variáveis

nome = 'Samuel'
sobrenome = 'Ferreira'
idade = 19
altura = 1.64
adulto = True

# Escrevendo no console.
print(nome)
print(sobrenome)
print(idade)
print(altura)
print(adulto)

# Concatenando informações
print('Meu nome é', nome)
print('Meu sobrenome é '+ sobrenome)
print('Meu nome completo é', nome, sobrenome)
print('Minha idade é {} e minha altura é {}'.format(idade, altura))

# Maneira moderna (baiana) de concatenar
print(f'Meu nome é {nome} e tenho {idade} anos de idade')

# Verificando o tipo da variável
print(type(nome))
print(type(sobrenome))
print(type(idade))
print(type(altura))
print(type(adulto))

# Expressões numéicas

numero1 = 10
numero2 = 5

soma = numero1 + numero2
sub = numero1 - numero2
mult = numero1 * numero2
div = numero1 / numero2

print(f'A soma é {soma}')
print(f'A subtração é {sub}')
print(f'A multiplicação é {mult}')
print(f'A divisão é {div}')

expressao = numero1 / (numero2 * numero2) + numero1
print(expressao)

# Outras operações

potencia = numero1**3
div_exata = numero1//4
print(potencia)
print(div_exata)