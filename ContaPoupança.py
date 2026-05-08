from Conta import Conta


class ContaPoupanca(Conta):

    def __init__(self, titular, saldo=0, extrato=None, investimento=0):

        super().__init__(titular, saldo, extrato)

        self.investimento = investimento

    def investir(self, valor):

        if valor <= 0:

            print("Valor inválido.")
            return

        if valor > self.saldo:

            print("Saldo insuficiente.")
            return

        self.saldo -= valor

        self.investimento += valor

        self._add_extrato("INVESTIMENTO", valor)

        print(f"R$ {valor:.2f} guardados no cofre.")

    def resgatar(self):

        if self.investimento <= 0:

            print("Nenhum valor investido.")

            return

        valor_resgate = (self.investimento + 10)

        self.saldo += valor_resgate

        self._add_extrato("RESGATE", valor_resgate)

        print(f"Resgate de R$ {valor_resgate:.2f} realizado.")

        print("Juros de R$ 10.00 aplicados.")

        self.investimento = 0