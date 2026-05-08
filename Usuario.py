from verificador_cpf import validar_cpf
import uuid
import json
import os
import time


class Usuario:

    def __init__(self, nome, cpf, idade, cidade, estado, pais, telefone, email, senha):

        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.cidade = cidade
        self.estado = estado
        self.pais = pais
        self.telefone = telefone
        self.email = email
        self.senha = senha


USUARIO_DADOS = "USUARIO_DADOS.json"


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def gerar_id():
    return str(uuid.uuid4())


def carregar_dados():

    try:

        with open( USUARIO_DADOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        return {}


def salvar_dados(dados):

    with open( USUARIO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump( dados, arquivo, indent=4, ensure_ascii=False)


def criando_conta():

    while True:

        limpar_tela()

        print("=" * 40)
        print("      ~~~~~~ CRIAÇÃO DE CONTA ~~~~~~")
        print("=" * 40)

        #NOME
        nome = input("Digite seu nome: ")

        # CPF
        while True:

            cpf = input("Digite o CPF (apenas números): ").strip()

            dados = carregar_dados()

            # 1 - 11 DÍGITOS
            if not cpf.isdigit() or len(cpf) != 11:
                
                print("\nCPF deve conter 11 números.")
                continue

            # 2 - CPF JÁ CADASTRADO
            if cpf in dados:
                
                print("\nCPF já cadastrado.")
                continue

            # 3 - CPF INVÁLIDO
            if not validar_cpf(cpf):
                
                print("\nCPF inválido.")
                continue

            break

        # IDADE
        while True:

            idade = input("Digite sua idade: ").strip()

            if idade.isdigit() and 18 <= int(idade) <= 120:

                idade = int(idade)
                break

            print("Idade inválida.")

        # TELEFONE
        while True:

            telefone = input("Digite seu telefone (11 dígitos): ").strip()

            if telefone.isdigit() and len(telefone) == 11:
                break

            print("Telefone inválido.")

        email = input("Digite seu e-mail: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        pais = input("País: ")

        # SENHA
        while True:

            senha = input("Crie uma senha com 6 dígitos: ").strip()

            if senha.isdigit() and len(senha) == 6:
                break

            print("Senha inválida.")

        # IDs DAS CONTAS
        id_conta_corrente = gerar_id()
        id_conta_poupanca = gerar_id()

        limpar_tela()

        print("=" * 40)
        print("       ~~~~~~ CONFIRME OS DADOS ~~~~~~")
        print("=" * 40)

        print(f"Nome              : {nome}")
        print(f"CPF               : {cpf}")
        print(f"Idade             : {idade}")
        print(f"Telefone          : {telefone}")
        print(f"E-mail            : {email}")
        print(f"Cidade            : {cidade}")
        print(f"Estado            : {estado}")
        print(f"País              : {pais}")

        print("\n======================== CONTAS ========================\n")

        print(f"ID Conta Corrente : {id_conta_corrente}")

        print(f"ID Conta Poupança : {id_conta_poupanca}")

        print("\n========================================================")
        print("\n1 - SALVAR")
        print("2 - REFAZER")

        opcao = input("\nEscolha: ")

        match opcao:

            case "1":

                dados = carregar_dados()

                dados[cpf] = {

                    "nome": nome,
                    "cpf": cpf,
                    "idade": idade,
                    "telefone": telefone,
                    "email": email,
                    "cidade": cidade,
                    "estado": estado,
                    "pais": pais,
                    "senha": senha,

                    "conta_corrente": {

                        "id": id_conta_corrente,
                        "saldo": 0
                    },

                    "conta_poupanca": {

                        "id": id_conta_poupanca,
                        "saldo": 0
                    }
                }

                salvar_dados(dados)
                
                limpar_tela()
                print("\nParabéns Conta criada com sucesso!")
                continue

            case "2":

                print("\nRefazendo cadastro...")
                continue

            case _:

                print("\nOpção inválida!")
                input("\nENTER para continuar...")


def acessar_conta():

    tentativas = 0

    dados = carregar_dados()

    while tentativas < 3:

        limpar_tela()

        print("=" * 40)
        print("      @@@@@@  LOGIN  @@@@@@")
        print("=" * 40)

        cpf = input("\nCPF: ")
        senha = input("Senha: ")

        if cpf in dados and dados[cpf]["senha"] == senha:
            
            limpar_tela()
            print(f"\nBem-vindo, {dados[cpf]['nome']}!")

            time.sleep(1) 
            limpar_tela()
            return dados[cpf]
            
        else:

            tentativas += 1

            print("\nLogin inválido.")

            print(f"Tentativas restantes: {3 - tentativas}")

            input("\nENTER para continuar...")

    print("\nConta bloqueada!")
    input("\nENTER para continuar...")