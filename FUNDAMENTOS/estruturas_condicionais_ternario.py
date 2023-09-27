"""
Estruturas condicionais
if (se)
else (senão)
"""
idade = 15
condicao = idade >= 18 #verdadeira
if idade <= 13:
    print("criança")
elif idade == 18:
    print("adolescente")
elif idade <= 30:
    print("adulto1")
else:
    print("adulto2")

#Operadores ternário

idade_vida = 50
#resultado = ('Menor idade','Maior idade')[idade_vida >= 18]
resultado = 'Maior idade' if idade_vida>=18 else 'Menor idade'
print(resultado)