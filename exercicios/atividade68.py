import uuid
import re
from datetime import datetime

# Módulo de validação
def validar_nome(nome):
    return len(nome.strip()) > 0

def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email) is not None

def validar_data_nascimento(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False

# Módulo de aluno
class Aluno:
    def __init__(self, nome, email, data_nascimento):
        self.nome = nome
        self.email = email
        self.data_nascimento = data_nascimento
        self.matricula = str(uuid.uuid4())[:8]  # matrícula única

    def __str__(self):
        return (f"\nMatrícula: {self.matricula}\n"
                f"Nome: {self.nome}\n"
                f"Email: {self.email}\n"
                f"Data de Nascimento: {self.data_nascimento}\n")

# Módulo de sistema
class SistemaCadastro:
    def __init__(self):
        self.alunos = []

    def cadastrar_aluno(self):
        nome = input("Digite o nome: ")
        if not validar_nome(nome):
            print("Nome inválido.")
            return

        email = input("Digite o e-mail: ")
        if not validar_email(email):
            print("E-mail inválido.")
            return

        data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
        if not validar_data_nascimento(data_nascimento):
            print("Data inválida.")
            return

        aluno = Aluno(nome, email, data_nascimento)
        self.alunos.append(aluno)
        print(f"Aluno cadastrado com sucesso! Matrícula: {aluno.matricula}")

    def atualizar_aluno(self):
        matricula = input("Digite a matrícula do aluno: ")
        aluno = self.buscar_aluno(matricula)
        if not aluno:
            print("Matrícula não encontrada.")
            return

        print("Digite os novos dados (deixe em branco para manter):")
        novo_nome = input("Novo nome: ")
        if novo_nome and validar_nome(novo_nome):
            aluno.nome = novo_nome

        novo_email = input("Novo e-mail: ")
        if novo_email and validar_email(novo_email):
            aluno.email = novo_email

        nova_data = input("Nova data de nascimento (dd/mm/aaaa): ")
        if nova_data and validar_data_nascimento(nova_data):
            aluno.data_nascimento = nova_data

        print("Dados atualizados com sucesso!")

    def excluir_aluno(self):
        matricula = input("Digite a matrícula do aluno: ")
        aluno = self.buscar_aluno(matricula)
        if aluno:
            self.alunos.remove(aluno)
            print("Aluno removido com sucesso!")
        else:
            print("Matrícula não encontrada.")

    def listar_alunos(self):
        if not self.alunos:
            print("Nenhum aluno cadastrado.")
        else:
            print("\nLista de Alunos:")
            for aluno in self.alunos:
                print(aluno)

    def mostrar_aluno(self):
        matricula = input("Digite a matrícula do aluno: ")
        aluno = self.buscar_aluno(matricula)
        if aluno:
            print("\nDados do Aluno:")
            print(aluno)
        else:
            print("Matrícula não encontrada.")

    def buscar_aluno(self, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                return aluno
        return None

# Módulo de menu
def menu():
    sistema = SistemaCadastro()

    while True:
        print("\nMENU")
        print("1 - Cadastrar aluno")
        print("2 - Atualizar aluno")
        print("3 - Excluir aluno")
        print("4 - Listar todos os alunos")
        print("5 - Mostrar aluno específico")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sistema.cadastrar_aluno()
        elif opcao == "2":
            sistema.atualizar_aluno()
        elif opcao == "3":
            sistema.excluir_aluno()
        elif opcao == "4":
            sistema.listar_alunos()
        elif opcao == "5":
            sistema.mostrar_aluno()
        elif opcao == "0":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

        continuar = input("\nDeseja realizar outra operação? (s/n): ")
        if continuar.lower() != "s":
            print("Encerrando o programa. Até logo!")
            break

# Execução
menu()