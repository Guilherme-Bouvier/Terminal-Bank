def menu_caixa():
    print("=" * 40)
    print("\n     $$$ ATM BANK $$$ \n")
    print("=" * 40)
    print("1 - CONTA CORRENTE")
    print("2 - CONTA POUPANÇA")
    print("4 - SAIR")

while True:
    menu_caixa()
    opcao = input("\n\nEscolha uma opção: ")

    match opcao:

        case "1":
            print("=" * 40)
            print("\n     $$$ CONTA CORRENTE $$$ \n")
            print("=" * 40)
            print("1 - SALDO")
            print("2 - DEPOSITO")
            print("3 - SAQUE")
            print("4 - TRANSFERENCI")
            print("5 - PAGAR CONTA")
            print("6 - SAIR")

            
            
        case "2":
            print("=" * 40)
            print("\n     $$$ CONTA POUPANÇA $$$ \n")
            print("=" * 40)
            print("1 - SALDO")
            print("2 - CAIXINHA")
            print("3 - INVESTIMENTO ")
            print("4 - RESGATAR")
            print("5 - SAIR")
