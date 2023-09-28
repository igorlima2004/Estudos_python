#Dicionários
"""
dicionario = {
    "correr" : 'Deslocar-se ou mover-se rapidamente',
    "ligar" : 'Estabelecer uma comunicação'
}

print(dicionario)
print(dicionario['correr'])
"""

carro = {
    'modelo':'Fusca',
    'marca': 'volkswagem',
    'ano': 1970,
    'donos': ['Igor', 'Kauanny']
}

print(type(carro))
print(carro['modelo'])
carro['donos'].append("Pedro")#adiciona os itens
print(carro['donos'][0])
carro['km'] = 8500
carro['ano'] = 1980
carro.update({'ano': 1980, 'km' : 8500})#atualiza os valores
del carro['ano']
carro.pop('ano') #apaga e guarda o valor passado
print(carro.keys()) #mostra as chaves
print(carro.values()) # mostra os valores
print(carro.items()) # mostra os itens
print(carro.get('ano','padrao')) #pega os itens que são relacionados
print(len(carro)) #conta a quantidade de itens
print(carro)
carro.clear()

#set -> Conjuto

itens = {"Igor","Pedro", "Matheus","João"}
print(type(itens))

carros = {"fusca", "gol","fiat147"}
carros2 = {"BMW", "fusca","passat"}
novo = carros.union(carros2) #Une os dois conjuntos
novo = carros.intersection(carros2) #Busca a intersecção entre os itens
carros.add("BMW") #Adiciona o item do comjunto
carros.remove("fusca") #Remove o item do conjunto
print(carros)