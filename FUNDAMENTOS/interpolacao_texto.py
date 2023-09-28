carro = "Velar"
preco = 1200.565

print('carro:' + carro + ', preço:' + str(preco))

# Versões mais antigas
"""
Formatações
%s -> Faz concatenação com variaveis str
%d -> Faz concatenação com variaveis int
%f -> Faz concatenação com variaveis float *com numero na frente  vc define quantidade de casas decimais
"""
print('carro: %s, preço: %.2f' % (carro, preco))
print('carro: {0}, preço: {1}' .format(carro, preco))

#Versão mais nova
print(f'carro: {carro}, preço: {preco}')
