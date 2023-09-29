"""
Funções
"""

#calcula média Igor
totalNotas = 5 + 7 + 5
media = totalNotas/ 3
print(f'Média do Igor é {media}')

#calcula média Kauanny
totalNotas = 10 + 7 + 10
media = totalNotas/ 3
print(f'Média da Kauanny é {media}')

def calcular_media(nome, nota1, nota2, nota3):
    totalNotas = nota1 + nota2 + nota3
    media = totalNotas/ 3
    print(f'Média da {nome} é {media}')

#calcula média Igor
calcular_media('Igor',8, 9, 10)

#calcula média Kauanny
calcular_media('Kauanny',10, 9, 10)


alunos = [
    {'nome': 'Igor', 'notas': [8, 9 ,10]},
    {'nome': 'Kauanny', 'notas': [10, 9 ,10]},
    {'nome': 'Pedro', 'notas': [10, 10 ,10]}
]

def calcular_media(notas):
    totalNotas = 0
    for nota in notas:
        totalNotas += nota
    media = totalNotas/ len(notas)
    return media

for aluno in alunos:
    nome  =  aluno['nome']
    notas = aluno['notas']
    media = calcular_media(notas)
    print(notas)
    print(f'Média do(a) {nome} é {media}')
