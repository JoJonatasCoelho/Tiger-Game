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

class Cliente:
    def __init__(self, *kwargs):
        self.__nome = nome
        self.__email = email
        self.__senha = senha

    def get_nome(self, id):
        return self.__nome

    def get_email(self, email):
        return self.__email

