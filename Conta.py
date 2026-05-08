class Conta:

    def __init__(self, titular, saldo=0, extrato=None):

        self.titular = titular
        self.saldo = saldo
        #Se extrato tiver algum valor, use ele. Senão, use uma lista vazia [].
        self.extrato = extrato if extrato else [] 

    def depositar(self, valor):

        if valor > 0:

            self.saldo += valor
            self._add_extrato("DEPÓSITO", valor)

            print(f"Depósito de R$ {valor:.2f} realizado.")

        else:
            print("Valor inválido.")

    def sacar(self, valor):

        if valor <= 0:
            print("Valor inválido.")
            return False

        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False

        self.saldo -= valor
        self._add_extrato("SAQUE", valor)

        print(f"Saque de R$ {valor:.2f} realizado.")

        return True

    def transferir(self, conta_destino, valor):

        if valor <= 0:
            print("Valor inválido.")
            return

        if valor > self.saldo:
            print("Saldo insuficiente.")
            return

        self.saldo -= valor
        conta_destino.saldo += valor

        self._add_extrato("TRANSFERÊNCIA ENVIADA", valor)
        conta_destino._add_extrato("TRANSFERÊNCIA RECEBIDA", valor)

        print("Transferência realizada com sucesso!")

    def _add_extrato(self, tipo, valor):

        self.extrato.append({
            "tipo": tipo,
            "valor": valor
        })

    def ver_extrato(self):

        print("\n========== EXTRATO ==========")

        if not self.extrato:
            print("Nenhuma movimentação.")
            return

        for e in self.extrato:
            print(f"{e['tipo']} -> R$ {e['valor']:.2f}")