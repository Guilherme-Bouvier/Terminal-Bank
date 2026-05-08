def mostrar_extrato(conta):
    print("=" * 30)
    print("\n  ~~~~~~EXTRATO ~~~~~~")
    print("=" * 30)
    for e in conta["extrato"]:
        print(f"{e['tipo']} R$ {e['valor']}")