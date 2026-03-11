"""
   Atributos = caracteristicas
   Ag: Número da agência (inteiro).
   CC: Número da conta corrente (inteiro).
   Saldo: Valor disponível (real).

   Métodos = o que essa conta faz?
    InicializaConta: Recebe os dados iniciais e prepara a conta para uso.
    Deposito: Recebe um valor e atualiza o saldo interno.
    Saque: Deduz um valor do saldo, garantindo que as regras de negócio sejam seguidas.
    Saldo: Retorna o valor atual para visualização, sem permitir alteração direta.
"""
from operator import truediv


class ContaCorrente:
    def __init__(self, nome, agencia, conta, saldo_inicial = 0):
        self.nome = nome
        self.agencia = agencia
        self.conta = conta
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Deposito de R${valor} realizado com sucesso.")
        else:
            print("Deposito invalido")

    def saque(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            return True
        else:
            print("Saldo insuficiente")
            return False

    def consultaSaldo(self):
        return self.__saldo


