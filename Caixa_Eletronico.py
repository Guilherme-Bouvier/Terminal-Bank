from ContaCorrente import ContaCorrente
from ContaPoupança import ContaPoupanca
from Usuario import carregar_dados, salvar_dados, limpar_tela


def menu_caixa(usuario):

    while True:

        limpar_tela()

        print("=" * 40)
        print("         $$$ ATM BANK $$$")
        print("=" * 40)

        print(f"Titular: {usuario['nome']}\n")

        print("1 - CONTA CORRENTE")
        print("2 - CONTA POUPANÇA")
        print("3 - SAIR")

        opcao = input("\nEscolha uma opção: ")

        match opcao:

            case "1":
                limpar_tela()
                menu_conta_corrente(usuario)

            case "2":
                limpar_tela()
                menu_conta_poupanca(usuario)

            case "3":
                limpar_tela()
                break

            case _:
                limpar_tela()
                print("\nOpção inválida.")
                input("\nENTER...")


def menu_conta_corrente(usuario):

    conta = ContaCorrente(
        usuario['nome'],
        usuario['conta_corrente']['saldo'],
        usuario['conta_corrente'].get('extrato', [])
    )
    while True:

        limpar_tela()

        print("=" * 40)
        print("        CONTA CORRENTE")
        print("=" * 40)

        print(f"Titular : {usuario['nome']}")

        print(f"ID Conta: {usuario['conta_corrente']['id']}" )

        print("\n1 - SALDO")
        print("2 - DEPÓSITO")
        print("3 - SAQUE")
        print("4 - TRANSFERÊNCIA")
        print("5 - EXTRATO")
        print("6 - VOLTAR")

        opcao = input("\nEscolha: ")

        match opcao:

            case "1":

                print(
                    f"\nSaldo atual: "
                    f"R$ {conta.saldo:.2f}"
                )

                input("\nENTER...")

            case "2":

                try:

                    valor = float(
                        input("Valor depósito: ")
                    )

                    conta.depositar(valor)

                    atualizar_conta(
                        usuario,
                        conta,
                        'conta_corrente'
                    )

                except ValueError:

                    print("\nDigite apenas números.")

                input("\nENTER...")

            case "3":

                try:

                    valor = float(
                        input("Valor saque: ")
                    )

                    conta.sacar(valor)

                    atualizar_conta(
                        usuario,
                        conta,
                        'conta_corrente'
                    )

                except ValueError:

                    print("\nDigite apenas números.")

                input("\nENTER...")

            case "4":

                transferir_por_id(
                    usuario,
                    conta,
                    'conta_corrente'
                )

            case "5":

                conta.ver_extrato()
                input("\nENTER...")

            case "6":
                break

            case _:

                print("\nOpção inválida.")
                input("\nENTER...")


def menu_conta_poupanca(usuario):

    conta = ContaPoupanca(
        usuario['nome'],
        usuario['conta_poupanca']['saldo'],
        usuario['conta_poupanca'].get('extrato', [])
    )

    while True:

        limpar_tela()

        print("=" * 40)
        print("        CONTA POUPANÇA")
        print("=" * 40)

        print(f"Titular : {usuario['nome']}")

        print(f"ID Conta: {usuario['conta_poupanca']['id']}")

        print("\n1 - SALDO")
        print("2 - INVESTIMENTO")
        print("3 - RESGATE")
        print("4 - TRANSFERÊNCIA")
        print("5 - EXTRATO")
        print("6 - VOLTAR")

        opcao = input("\nEscolha: ")

        match opcao:

            case "1":

                print(
                    f"\nSaldo atual: "
                    f"R$ {conta.saldo:.2f}"
                )

                input("\nENTER...")

            case "2":

                try:

                    valor = float(
                        input("Valor investimento: ")
                    )

                    conta.investir(valor)

                    atualizar_conta(
                        usuario,
                        conta,
                        'conta_poupanca'
                    )

                except ValueError:

                    print("\nDigite apenas números.")

                input("\nENTER...")

            case "3":

                conta.resgatar()

                atualizar_conta(
                    usuario,
                    conta,
                    'conta_poupanca'
                    )

                input("\nENTER...")





            case "4":

                transferir_por_id(
                    usuario,
                    conta,
                    'conta_poupanca'
                )

            case "5":

                conta.ver_extrato()
                input("\nENTER...")

            case "6":
                break

            case _:

                print("\nOpção inválida.")
                input("\nENTER...")


def atualizar_conta(usuario, conta_obj, tipo_conta):

    dados = carregar_dados()

    cpf = usuario['cpf']

    dados[cpf][tipo_conta]['saldo'] = conta_obj.saldo

    dados[cpf][tipo_conta]['extrato'] = conta_obj.extrato

    salvar_dados(dados)

    usuario[tipo_conta]['saldo'] = conta_obj.saldo

    usuario[tipo_conta]['extrato'] = conta_obj.extrato


def transferir_por_id(
    usuario,
    conta_obj,
    tipo_conta
):

    dados = carregar_dados()

    try:

        id_destino = input(
            "ID da conta destino: "
        )

        valor = float(
            input("Valor transferência: ")
        )

    except ValueError:

        print("\nDigite apenas números.")
        input("\nENTER...")
        return

    for cpf_destino, dados_usuario in dados.items():

        for conta_nome in [
            'conta_corrente',
            'conta_poupanca'
        ]:

            conta = dados_usuario[conta_nome]

            if conta['id'] == id_destino:

                if valor > conta_obj.saldo:

                    print("\nSaldo insuficiente.")
                    input("\nENTER...")
                    return

                conta_obj.saldo -= valor

                conta['saldo'] += valor

                dados[cpf_destino][conta_nome]['saldo'] = conta['saldo']

                conta_obj._add_extrato(
                    'TRANSFERÊNCIA ENVIADA',
                    valor
                )

                if 'extrato' not in conta:

                    conta['extrato'] = []

                conta['extrato'].append({

                    "tipo": (
                        "TRANSFERÊNCIA "
                        "RECEBIDA"
                    ),

                    "valor": valor
                })



                salvar_dados(dados)

                atualizar_conta(
                    usuario,
                    conta_obj,
                    tipo_conta
                )

                print(
                    "\nTransferência "
                    "realizada!"
                )   

                input("\nENTER...")

                usuario_atualizado = carregar_dados()[usuario['cpf']]

                usuario.update(usuario_atualizado)

                return

    print("\nConta destino não encontrada.")
    input("\nENTER...")