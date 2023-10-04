#Métodos
#cadastro email: ig@gmail.com senha:1234

class Usuario:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def __str__(self):
        return f'email: {self.email}, senha: {self.senha}'

    def _validar(self):#metodo _privado
        email_cadastrado = 'ig@gmail.com'
        senha_cadastrado = '1234'

        if email_cadastrado == self.email and senha_cadastrado == self.senha:
            print('Usuario validado')
        else:
            print('Email ou senha incorretos')

    def forca_senha(self):
        if len(self.senha) > 5:
            return True
        else:
            return False
        
    def cadastrar_endereco(self, endereco1, endereco2):
        print(f'Endereços: {endereco1}, {endereco2}')

    def logar(self):
        self._validar()
        print('enviar para a tela principal')

usuario = Usuario('ig@gmail.com', '1234')#caixa de texto

usuario.logar()
print(usuario)
if usuario.forca_senha():
    print('Senha Forte')
else:
    print('Senha Fraca')
usuario.cadastrar_endereco('Rua 1', 'Rua 2')