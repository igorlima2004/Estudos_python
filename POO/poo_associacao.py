"""
Relação de Associação -> É uma das relações mais comuns
entre dois objetos, acontece quando um objeto "utiliza"
outro, porém, sem que eles dependam um do outro
"""
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.video_game = None

    def andar(self):
        print(f'Jogador {self.nome} andando')

class VideoGame:
    def __init__(self, nome):
        self.nome = nome

    def rodar_jogo(self):
        print(f'Rodar jogo no {self.nome}')

jogador = Jogador('Igor')
videogame = VideoGame('Ps4')

jogador.video_game = videogame
jogador.video_game.rodar_jogo()