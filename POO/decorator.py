def passo1(p1):
    p1 = f'--{p1}--'

    def passo2(p2):
        return f'{p1} e {p2}'
    
    return passo2

funcao_p2 = passo1('Abrir a porta')
print(funcao_p2('Entrar no quarto'))

def verifica_usuario_logado(p_funcao):#Função Decorator
    def verifica():
        print('[30 - Antes vamos verificar se o usuário está logado]')
        retorno =  p_funcao()
        print('[FIM]')
        return retorno
    
    return verifica()

@verifica_usuario_logado #Decorator
def salvar_postagem():
    print('...[executando]')
    print('Postagem criada')

@verifica_usuario_logado #Decorator
def salvar_comentario():
    print('...[executando]')
    print('Comentário criado')

salvar_postagem()
salvar_comentario()