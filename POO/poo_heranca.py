#Herança - Reutilização e manutenção
#Classe: Cao Passaro
class Animal:
    def  __init__(self):
        self.cor = ''
        self.tamanho = ''
        self.peso = ''

    def correr(self):
        print('correr')

    def dormir(self):
        print('dormir')

class Cao(Animal):

    def latir(self):
        print('latir')

class Passaro(Animal):#subclasse , classe filha

    def voar(self):
        print('voar')

cao = Cao()
cao.cor = 'Preto'
cao.correr()
print(cao.cor)

passaro = Passaro()
passaro.cor = 'Amarelo'
passaro.correr()
print(passaro.cor)