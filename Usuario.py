import json

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


def carregar_dados():
    # Leitura Dados
    try:
        with open(USUARIO_DADOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}


def salvar_dados(dados):
    # Criação de dados
    with open(USUARIO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def criando_conta():
    nome = input("Digite seu nome: ")

    # CPF
    while True:
        cpf = input("Digite o CPF (apenas números): ").strip()
        if cpf.isdigit() and len(cpf) == 11:
            break
        print("CPF inválido.")

    # Idade
    while True:
        idade = input("Digite sua idade: ").strip()
        if idade.isdigit() and 18 <= int(idade) <= 120:
            idade = int(idade)
            break
        print("Idade inválida.")

    # Telefone
    while True:
        telefone = input("Digite seu telefone (11 dígitos): ").strip()
        if telefone.isdigit() and len(telefone) == 11:
            break
        print("Telefone inválido.")

    email = input("Digite seu e-mail: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    pais = input("País: ")
     # Senha
    while True:
        senha = input("Crie uma senha com 6 dígitos (apenas números): ").strip()
        if senha.isdigit() and len(senha) == 6:
            break
        print("Senha inválida.")

    dados = carregar_dados()

    dados[email] = {
        "nome": nome,
        "cpf": cpf,
        "idade": idade,
        "telefone": telefone,
        "cidade": cidade,
        "estado": estado,
        "pais": pais,
        "senha": senha
    }

    salvar_dados(dados)

    print("Conta criada com sucesso!")


def acessar_conta():
    tentativas = 0
    dados = carregar_dados()

    while tentativas < 3:
        cpf = input("Cpf: ")
        senha = input("Senha: ")

        if cpf in dados and dados[cpf]["senha"] == senha:
            print(f"Bem-vindo, {dados[cpf]['nome']}!")
            return dados [cpf]
        
        else:
            tentativas += 1
            print("Login inválido.")

    print("Conta bloqueada!")
    
# def trocar_senha ():