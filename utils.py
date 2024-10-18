def ler_dinheiro():
    dinheiro = int(input("Digite a quantidade de dinheiro necessária: R$"))
    return dinheiro

class Saldo:
    def __init__(self, saldo):
        self.__saldo = saldo

    def setter(self, nsaldo):
        self.__saldo = nsaldo

    def getter(self):
        return self.__saldo
