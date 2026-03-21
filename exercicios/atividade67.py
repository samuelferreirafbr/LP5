def exibir_tabuleiro(tabuleiro):
    print("\n")
    for i in range(3):
        print(" | ".join(tabuleiro[i]))
        if i < 2:
            print("-" * 5)
    print("\n")


def verificar_vitoria(tabuleiro, jogador):
    linhas = tabuleiro
    colunas = [[tabuleiro[i][j] for i in range(3)] for j in range(3)]
    diagonais = [[tabuleiro[i][i] for i in range(3)],
                 [tabuleiro[i][2 - i] for i in range(3)]]

    for grupo in linhas + colunas + diagonais:
        if all(celula == jogador for celula in grupo):
            return True
    return False


def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    jogadas = 0

    while True:
        exibir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}")

        try:
            linha = int(input("Digite a linha (0, 1, 2): "))
            coluna = int(input("Digite a coluna (0, 1, 2): "))
        except ValueError:
            print("Entrada inválida. Digite números entre 0 e 2.")
            continue

        if linha not in [0, 1, 2] or coluna not in [0, 1, 2]:
            print("Posição inválida. Tente novamente.")
            continue

        if tabuleiro[linha][coluna] != " ":
            print("Essa posição já está ocupada. Escolha outra.")
            continue

        tabuleiro[linha][coluna] = jogador_atual
        jogadas += 1

        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break

        if jogadas == 9:
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"


def menu():
    while True:
        print("Bem-vindo ao Jogo da Velha!")
        print("Escolha uma opção:")
        print("1 - Jogar")
        print("0 - Sair")

        opcao = input("Digite sua escolha: ")

        if opcao == "1":
            print("Iniciando o jogo...")
            jogo_da_velha()
            continuar = input("Deseja jogar novamente? (s/n): ")
            if continuar != "s":
                print("Encerrando o programa. Até logo!")
                break
        elif opcao == "0":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()