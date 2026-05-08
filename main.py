from Usuario import criando_conta, acessar_conta, limpar_tela
from historia import historia_bank
from Caixa_Eletronico import menu_caixa
import time


def menu():
    print("=" * 30)
    print("     TERMINAL BANK")
    print("=" * 30)
    print("1 - ENTRAR")
    print("2 - CRIAR CONTA")
    print("3 - HISTÓRIA")
    print("4 - SAIR")
    print("=" * 30)

menu()

while True:
    limpar_tela()
    menu()
    op = input("Escolha: ")

    match op:

        case "1":
            limpar_tela()
            usuario = acessar_conta()

            if usuario:
                menu_caixa(usuario)

        case "2":
            limpar_tela()
            criando_conta()
            input("\nENTER para continuar...")
            time.sleep(0.5)

        case "3":
            limpar_tela()
            historia_bank()
            input("\nENTER para voltar...")

        case "4":
            print("Saindo...")
            break

        case _:
            print("Opção inválida!")
            time.sleep(1)