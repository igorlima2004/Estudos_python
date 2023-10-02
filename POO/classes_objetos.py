"""
notação Pascal Case: ContaBancaria
notação Camel Case: contaBancaria
notação Snake Case: conta_bancaria
"""

class ContaBancaria:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo


    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor


conta = ContaBancaria("Igor", 1000)
conta.depositar(200)
conta.sacar(100)
print(f'nome: {conta.nome} - saldo: R$ {conta.saldo}')