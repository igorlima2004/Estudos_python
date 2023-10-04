from abc import ABC, abstractmethod
class Animal(ABC):#Classe Abstrata

    def correr(self):
        print('Correr')

    @abstractmethod
    def respirar(self):
        pass


class Cao(Animal):
    def respirar(self):
        print('respirar como um cão')

class Passaro(Animal):
    def respirar(self):
        print('respirar como um pássaro')

#animal = Animal()
#animal.correr()
cao = Cao()
cao.correr()
cao.respirar()

"""
Conta bancária
Conta, Conta corrente e conta poupança
"""
class Conta(ABC):
    def __init__(self, numero_conta, saldo):
        self._numero_conta = numero_conta
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass

class ContaPoupanca(Conta):
    def __init__(self, numero_conta, saldo):
        super().__init__(numero_conta, saldo)

    def sacar(self, valor):
        limite = 300
        if valor <= limite:
            self._saldo -= valor
        else:
            print('Limite excedido(300)')

class ContaCorrente(Conta):
    def __init__(self, numero_conta, saldo):
        super().__init__(numero_conta, saldo)

    def sacar(self, valor):
        limite = 600
        if valor <= limite:
            self._saldo -= valor
        else:
            print('Limite excedido(600)')

conta_poupanca = ContaPoupanca(10548, 1000)
conta_poupanca.depositar(200)#1200
conta_poupanca.sacar(200)#1000
print(conta_poupanca)

conta_corrente = ContaCorrente(10548, 1000)
conta_corrente.depositar(200)#1200
conta_corrente.sacar(200)#1000
print(conta_corrente)