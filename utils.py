def ler_dinheiro():
    dinheiro = int(input("Digite a quantidade de dinheiro necessária: R$"))
    return dinheiro

class Saldo:
    def __init__(self, saldo = 0):
        self.__saldo = saldo

    def setter(self, nsaldo):
        self.__saldo = nsaldo

    def getter(self):
        return self.__saldo

class Cliente:
    def __init__(self, credentials):
        infos = *credentials
        self.__nome = infos["nome"]
        self.__email = infos["email"]
        self.__senha = infos["senha"]

        __saldo_cliente = Saldo()

    def get_nome(self, id):
        return self.__nome

    def get_email(self, email):
        return self.__email


