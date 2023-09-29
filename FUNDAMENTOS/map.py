lista_numero = [10, 20, 30]

#nova_lista = map(lambda n: n * 2, lista_numero)
#print(list(nova_lista))

lista = [
    {'produto': 'Fone de Ouvido', 'preço': 500},
    {'produto': 'Controle de Ps4', 'preço': 400},
    {'produto': 'Celular', 'preço': 800},
]

def calcular_desconto(produto):
    produto['preço'] = produto['preço'] - 10

carrinho_lista = map(calcular_desconto, lista)