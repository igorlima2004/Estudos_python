lista = ['Jamilton', 'Ana']
dicionario = {'nome': 'Jamilton'}

try:#tentar
    print(lista[1])
    #print(lista[3])
    #print(dicionario['teste'])
except (IndexError, KeyError) as erro: # Exceto
    print('Item selecionado fora lista')
except Exception as erro: # Exceto
    print(f'Exception: {erro}')
else:
    print('Executou com sucesso!')
finally:
    print('Sempre executada, independente de erro ou não')

print('Continua executando')