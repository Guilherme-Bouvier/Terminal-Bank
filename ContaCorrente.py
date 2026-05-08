from Conta import Conta

class ContaCorrente(Conta):

    def sacar(self, valor):

        taxa = 5
        valor_total = valor + taxa

        if valor_total > self.saldo:
            print("Saldo insuficiente.")
            return False

        self.saldo -= valor_total

        self._add_extrato("SAQUE + TAXA", valor_total)

        print(f"Saque de R$ {valor:.2f} realizado.")

        print(f"Taxa ATM: R$ {taxa:.2f}")

        return True