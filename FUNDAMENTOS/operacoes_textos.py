#Operações com textos
texto = "carro"
print(texto)
print(texto[4])
print(texto[-5])
print(texto[2:4])
print(texto[::3])

#frase = 'Meu nome é \'Igor\''
#frase = 'Meu nome é \n\tIgor' #quebra linha
frase = """
  Igor
    teste
        ...
"""

print(frase)

frase2 = 'Meu nome é Igor'
print("nome" in frase )
print( len(frase2))
print( frase2.lower() )
print( frase2.upper() )
print( frase2.capitalize() )
print( frase2.split() )
