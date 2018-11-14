import random

class Feiticos:

    def __init__(self, nome, custo, dano, tipo):
        self.nome = nome
        self.custo = custo
        self.dano = dano
        self.tipo = tipo

    def gerar_dano_magico(self):
        low = self.dano - 15
        high = self.dano + 15
        return random.randrange(low, high)
