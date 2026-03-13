# Condicional if
# 'elif' = 'else if'
# and, or e not

# acompanhada = 'não'
# idade = 18

# # if idade >= 18:
# #     print('Você pode assistir ao filme')
# # elif (idade >= 15 and idade <=17) and acompanhada == 'sim':
# #     print('Você pode assistir ao filme')
# # else:
# #      print('Você não pode assistir')

# Switch-Case = Match-Case
# Case _ = else final

print('0 - cadastrar')
print('1 - editar')
print('2 - excluir')

opcao = int(input('O que deseja realizar? '))

match opcao:
    case 0:
        print('Você escolheu cadastrar')
    case 1:
        print('Você escolheu editar')
    case 2:
        print('Você escolheu excluir')
    case _:
        print('Opção inválida')