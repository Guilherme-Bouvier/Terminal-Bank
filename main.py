from Usuario import criando_conta, acessar_conta
from Conta import Conta
from historia import historia_bank
from Caixa_Eletronico import menu_caixa


import time
tempo = 3

conta = Conta("Guilherme")


def menu_inicial():
    print("=" * 30)
    print("\n     +++ TERMINAL BANK +++ \n")
    print("=" * 30)
    print("1 - ENTRAR")
    print("2 - CRIAR CONTA")
    print("3 - CONHEÇA NOSSA HISTÓRIA")
    print("4 - SAIR")


while True:
    menu_inicial()
    opcao = input("\n\nEscolha uma opção: ")

    match opcao:
        case "1":
            print("=" * 40)
            print("\n     $$$ ACESSANDO MINHA CONTA $$$ \n")
            print("=" * 40)
            print ("\n")
            acessar_conta()
            
            time.sleep(tempo)

        case "2":
            print("=" * 40)
            print("\n     $$$ CRIANDO CONTA $$$ \n")
            print("=" * 40)
            print ("\n")
            criando_conta()

        case "3":
            print("=" * 100)
            print("\n                                  $$$ CONHEÇA NOSSA HISTÓRIA $$$ \n")
            print("=" * 100)
            print ("\n")
            historia_bank()
            time.sleep(8)

        case "4":
            print("Saindo...")
            break

        case _:
            print("Opção inválida!")