"""
Polimorfismo -> Qualidade ou estado de ser capaz de 
assumir diferentes formas
Poli -> muitas
morfo -> formas
"""
class Animal:
    def  __init__(self, cor, tamanho, peso):
        self.cor = cor
        self.tamanho = tamanho
        self.peso = peso

    def correr(self):
        print('correr como um')

    def dormir(self):
        print('dormir')

    def __str__(self) -> str:
        return f'cor {self.cor}, tamanho:{self.tamanho}, peso: {self.peso}'
    
class Cao(Animal):
    def __init__(self, cor, tamanho, peso, raca):
        super().__init__(cor, tamanho, peso)
        self.peso = f'{peso} Kg'
        self.raca = raca

    def latir(self):
        print('latir')

    #Sobrescrita de método -> override
    def correr(self):
        super().correr()
        print('cão')

    def __str__(self):
        return super().__str__()+ f', raça: {self.raca}'

class Passaro(Animal):#subclasse , classe filha
    def __init__(self, cor, tamanho, peso):
        super().__init__(cor, tamanho, peso)

    def voar(self):
        print('voar')

    def correr(self):
        super().correr()
        print('passaro')

class Papagaio(Passaro):
    def __init__(self, cor, tamanho, peso):
        super().__init__(cor, tamanho, peso)

    def falar(self):
        print('falar')

cao = Cao('Marrom', '40cm', '1', 'Golden')
print(cao)
cao.correr()

passaro = Passaro('Amarelo', '30cm', '500kg')
print(passaro)
passaro.correr()

papagaio = Papagaio()
papagaio.correr()
papagaio.voar()
papagaio.falar()