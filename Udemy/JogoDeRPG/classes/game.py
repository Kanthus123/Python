import random

class bcolors:  #Não funciona no Windows sem a biblioteca colorama. Esse problema não é citado na aula devido ao professor estar usando MAC e não estar ciente de tal problema!

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Pessoa:

    def __init__(self, nome, hp, mp, atk, defe, magia, itens):
        self.nome = nome
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.defe = defe
        self.magia = magia
        self.itens = itens
        self.acao = ["Ataque", "Magia", "Items"]

    def gerar_dano(self):
        return random.randrange(self.atkl, self.atkh)

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
            print(str(i) + ":", feitico.nome, "(Custo:", str(feitico.custo) + ")")
            i += 1

    def escolher_itens(self):
        i = 1
        print(bcolors.HEADER + "\nItens" + bcolors.ENDC)
        for item in self.itens:
            print(str(i) + ":", item["item"].nome, ":", item["item"].descricao, " (x", item["quantidade"], ")")
            i += 1

    def get_status(self):
        print("                        _________________________       __________")
        print(bcolors.BOLD + self.nome + ":        " +
              str(self.hp) + "/" + str(self.max_hp) + "|" + bcolors.OKGREEN + "█████████████████████████" + bcolors.ENDC + bcolors.BOLD + "|" +
              str(self.mp) + "/" + str(self.max_mp) + "|" + bcolors.OKBLUE + "██████████" + bcolors.ENDC + "|")
