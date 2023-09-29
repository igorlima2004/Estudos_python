from functools import reduce
#Reduce (reduzir) -> acumula e reduz uma lista em um único valor
# não vem dentro do bultins

lista_numero = [10, 10, 10]


#acumula = 0
#for item in lista_numero:
#    acumula = acumula + item
#    acumula += item

#print(acumula)
funcao = lambda acumulador, item : acumulador + item
resultado = reduce(funcao, lista_numero, 0 )
print(resultado)

lista = [
    {'produto': 'Fone de Ouvido', 'preço': 500},
    {'produto': 'Controle de Ps4', 'preço': 400},
    {'produto': 'Celular', 'preço': 800},
]

funcao1 = lambda acumulador, produto : acumulador + produto['preço']
resultado1 = reduce(funcao1, lista, 0 )
print(resultado1)