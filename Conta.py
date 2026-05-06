from Usuario import Usuario

class Conta:
    
    def __init__(self, titular):
        self.titular = titular
        self.__saldo = 0

    def get_saldo(self):
        return self.__saldo
    
    def depositar(self, valor):
        if valor <= 0:
            print ("Valor invalido")
        else:
            self.__saldo += valor
            print ("Depósito realizado!")


    def sacar (self, valor):
        if valor <= 0:
            print ("Valor invalido")
        else:
            self.__saldo -= valor
            print ("Depósito realizado!")