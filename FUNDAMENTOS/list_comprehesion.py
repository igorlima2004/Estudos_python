"""
List Comprehension (compreensão de lista) ->
É uma construção sintática para
criação de uma lista baseada em listas existentes.
"""


lista = [ 10, 20, 30]
nova_lista = [ item * 2 for item in lista]
#nova_lista = map(lambda n: n * 2, lista)
#print(list(nova_lista))

#usada como filter
nova_lista = [item for item in lista if item >= 20]
print(nova_lista)

#usada como dicionario
lista = [ 10, 20, 30]
dicionario = {f'chave{i}': i for i in lista}
print(dicionario)