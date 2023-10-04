"""
Atributo de classe
Atributo de instância
"""
class Pessoa:
    planeta = 'terra'
    def __init__(self):
        self.nome = 'sem nome'

    def exibir_nome(self):
        print(f'Nome: {self.nome}')
igor = Pessoa()
igor.nome = 'Igor'
print(igor.nome)

pedro = Pessoa()
pedro.nome = 'Pedro'
print(pedro.nome)

"""
Método de classe
Método de instância
"""
class Pessoa:
    planeta = 'terra'
    def __init__(self, nome):
        self.nome = nome 

    #vê apenas instância
    def exibir_nome(self):
        print(f'Nome: {self.nome}')

    #vê apenas classe
    @classmethod
    def exibir_planeta(cls):
        print(f'Planeta: {cls.planeta}')

    #Não sabe nada sobre a classe ou instância
    @staticmethod
    def recuperar_planetas_habitaveis():
        print('Terra e Marte')

Pessoa.exibir_planeta()
Pessoa.recuperar_planetas_habitaveis('Igor')
igor = Pessoa('Igor')
igor.exibir_nome()

pedro = Pessoa('Pedro')
pedro.exibir_nome()