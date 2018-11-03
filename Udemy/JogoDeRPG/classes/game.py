import random

class bcolors:  #Não funciona no Windows sem a biblioteca colorama

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Pessoa:

    def __init__(self, hp, mp, atk, defe, magia):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.defe = defe
        self.magia = magia
        self.acao = ["Ataque", "Magia"]

    def gerar_dano(self):
        return random.randrange(self.atkl, self.atkh)

    def gerar_dano_feitico(self, i):
        mgl = self.magia[i]["dmg"] - 5
        mgh = self.magia[i]["dmg"] + 5
        return random.randrange(mgl, mgh)

    def curar(self, cura):
        self.hp += cura
        if  self.hp > self.max_hp:
            self.hp = self.max_hp
        return self.hp

    def receber_dano(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def reduzir_mp(self, custo):
        self.mp -= custo

    def get_nome_feitico(self, i):
        return self.magia[i]["nome"]

    def get_custo_feitico(self, i):
        return self.magia[i]["custo"]

    def escolher_acao(self):
        i = 1
        print(bcolors.HEADER + "Ações" + bcolors.ENDC)
        for item in self.acao:
            print(str(i) + ":", item)
            i += 1

    def escolher_magia(self):
        i = 1
        print(bcolors.HEADER + "\nMagias" + bcolors.ENDC)
        for feitico in self.magia:
            print(str(i) + ":", feitico["nome"], "(Custo:", str(feitico["custo"]) + ")")
            i += 1
