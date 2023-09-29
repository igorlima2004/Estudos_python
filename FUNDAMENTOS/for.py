postagens = [
    "Hoje passeado pela avenida paulista",#0
    "Fazendo trilha na pedra do Gavião",#1
    "Hoje fiz um curso de criação de Sistemas",#2
    "Na casa da mãe, almoçando todos juntos",#3
]

for postagem in postagens:
    print(postagem)
    print("+++++++")

#nome, nome2 = "Igor", "Igor2"

#for postagem in enumerate(postagens):
#    print(f'{indice} - {postagens}')
#    print("+++++++")

#for indice in range(0,11): #(1,11)
#    print(indice)


#Percorrendo textos, tuplas , set

palavra = "jamilton"
for letra in palavra:
    print(f' - {letra} - ')


meses = ('Janeiro', 'Fevereiro','Março')
for mes in meses:
    print(f' - {mes} - ')


frutas = {'banana', 'maça', 'abacaxi', 'melancia'}
for fruta in frutas:
    print(f' - {fruta} - ')