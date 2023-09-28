"""
Listas são como arrays em Js
Mutável e dinâmica, heterogênea e indexada
"""
lista = ["Igor","Pedro", "Matheus","João"]
print(type(lista))
print( lista[0] )
print( lista[-1] )
print( lista[0:2] )
print( lista[::2] )

#lista[2] = "Alterado"
#lista.append("Novo")
#lista.remove("Pedro")
#del lista[0:2]
print( len(lista) )
print( lista.count("Igor") )
print( lista.index("Pedro") )
#lista.clear()
#lista.reverse()
#lista.sort()
print(lista)
print("Igor" in lista)
print("Victor" not in lista)