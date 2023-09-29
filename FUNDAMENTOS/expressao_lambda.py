#Expressão Lambda ( Função Anômina )

def subtrair(a, b):
    return a - b

#variavel= subtrair
#print(subtrair(1, 3))

#sub = lambda a, b: print(f'resultado: {a - b}')
#print(sub(1, 3))
#sub(1, 3)

lista = [
    {'produto': 'Fone de Ouvido', 'preço': 500},
    {'produto': 'Controle de Ps4', 'preço': 400},
    {'produto': 'Celular', 'preço': 800},
]

def calcular_desconto(lista, funcao):
    total = 0
    for produto in lista:
        item_desconto = funcao(produto['preço'], 10)
        total += item_desconto
        print(item_desconto)
    print(f'total: {total}')

calcular_desconto(lista, lambda a, b : a - b )