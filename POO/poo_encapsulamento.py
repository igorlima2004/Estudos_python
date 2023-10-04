"""
Pilar2 - Encapsulamento
"""
class Filtro:
    def __init__(self, img):
        self.img = img
    
    def preto_e_branco(self):
        print(f'{self.img} com filtro preto e branco')

    def foto_envelhecida(self):
        print(f'{self.img} com filtro envelhecido')

filtro = Filtro('foto_igor')
filtro.preto_e_branco()

#Controle de acesso Getter e Setters
class ContaBancaria:
    def __init__(self, saldo):
        self._numero = 0
        self.saldo = saldo

    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self):
        return self._numero

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

conta = ContaBancaria(800)
conta.numero = 10589
print(conta.numero)
#conta.sacar(100)
#conta.depositar(200)
#print(conta.saldo)