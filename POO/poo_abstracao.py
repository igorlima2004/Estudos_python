"""
Pilar1 - Abstração (Venda de peças e Uber)
Modelo, Entidade, Identidade
Características e ações
"""

class Carro:
    def __init__(self, modelo, cor, placa):
        self.modelo = modelo
        self.cor = cor
        self.placa = placa


    def exibir_local_atual(self):
        print('Carro esta na rua 10')

carro = Carro("Mercedes", "Preto", "JHM-6854")

#carro_matheus = Carro("BMW", "Vermelho", "RTM-2345")

#Loja Virtual
class Produto:
    #roupas
    def __init__(self, tamanho, cor, preco):
        self.tamanho = tamanho
        self.cor = cor
        self.preco = preco
    #eletrônicos
    def __init_(self, altura, largura, cor, preco):
        self.altura = altura
        self.largura = largura
        self.cor = cor
        self.preco = preco

produto = Produto("P", "preto", 25.60)
produto = Produto("50cm", "80cm", "preto", 50.60)