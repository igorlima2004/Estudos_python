"""
Operadores relacionais (retorna verdadeiro ou falso)
== (igual a)
!= (diferente)
>  (maior que)
<  (menor que)
>= (maior ou igual)
<= (menor ou igual)
""" 
#print(1 == 1)
#print(1 != 2)
#print(3 > 2)
#print(1 >= 2)
idade = 10
print(idade >= 18 )

"""
Operadores lógicos (testa condições com true ou false)
and (e) &&
or  (ou) ||
"""
# idade > 50 ou totalCompra > 200 20%
idade = 50
totalCompra = 100
print( idade >= 50 or totalCompra >= 200)
print( idade >= 50 and totalCompra >= 200)