# Filter -> filtrar dados
"""
expressão Verdadeira ou Falso
ex:
numero > 20

10 - false
20 - false
30 - true
"""

#lista_numero = [10, 20, 30]
#nova_lista = filter(lambda n: n >= 20, lista_numero)
#print(list(nova_lista))

lista = [
    {'produto': 'Fone de Ouvido', 'preço': 500},
    {'produto': 'Controle de Ps4', 'preço': 400},
    {'produto': 'Celular', 'preço': 800},
]

nova_lista = filter(lambda p: p['preço'] >= 500, lista)
print(list(nova_lista))