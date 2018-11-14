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
        print("\n" + bcolors.BOLD + self.nome + bcolors.ENDC)
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

    def escolher_alvo(self, inimigos):
        i = 1
        print("\n"+ bcolors.FAIL + bcolors.BOLD + "ALVO:" + bcolors.ENDC)
        for inimigo in inimigos:
            if inimigo.get_hp() != 0:
                print(" " + str(i) + ".", inimigo.nome)
                i += 1
        escolha= int(input("Escolha o alvo:")) - 1
        return escolha


    def get_status_inimigo(self): #status dos inimigos
        barra_hp = ""
        barra_ticks = (self.hp / self.max_hp) * 100  / 2

        while barra_ticks > 0:
            barra_hp += "█"
            barra_ticks -= 1

        while len(barra_hp) < 50:
            barra_hp += " "

        hp_string = str(self.hp) + "/" + str(self.max_hp)
        hp_atual = ""

        if len(hp_string) < 11:
            decrementa = 11 - len(hp_string)

            while decrementa > 0:
                hp_atual += " "
                decrementa -= 1

            hp_atual += hp_string
        else:
            hp_atual = hp_string

        print("                                  __________________________________________________")
        print(bcolors.BOLD + self.nome + ":        " +
              hp_atual + "|" + bcolors.FAIL + barra_hp + bcolors.ENDC + "|")

    def get_status(self): #status dos jogadores
        barra_hp = ""
        barra_mp = ""
        barra_ticks = (self.hp / self.max_hp) * 100  / 4
        barra_ticks_mp = (self.mp / self.max_mp) * 100  / 10


        while barra_ticks > 0:
            barra_hp += "█"
            barra_ticks -= 1

        while len(barra_hp) < 25:
            barra_hp += " "

        while barra_ticks_mp > 0:
            barra_mp += "█"
            barra_ticks_mp -= 1

        while len(barra_mp) < 10:
            barra_mp += " "

        hp_string = str(self.hp) + "/" + str(self.max_hp)
        hp_atual = ""

        if len(hp_string) < 9:
            decrementa = 9 - len(hp_string)

            while decrementa > 0:
                hp_atual += " "
                decrementa -= 1

            hp_atual += hp_string
        else:
            hp_atual = hp_string

        mp_string = str(self.mp) + "/" + str(self.max_mp)
        mp_atual = ""

        if len(mp_string) < 7:
            decrementa = 7 - len(mp_string)

            while decrementa > 0:
                mp_atual += " "
                decrementa -= 1

            mp_atual += mp_string
        else:
            mp_atual = mp_string

        print("                          _________________________             __________")
        print(bcolors.BOLD + self.nome + ":        " +
              hp_atual + "|" + bcolors.OKGREEN + barra_hp + bcolors.ENDC + bcolors.BOLD + "|    " +
              mp_atual + "|" + bcolors.OKBLUE + barra_mp + bcolors.ENDC + "|")


    def escolher_feitico_inimigo(self):
        escolha_magia = random.randrange(0, len(self.magia))
        feitico = self.magia[escolha_magia]
        dano_magico = feitico.gerar_dano_magico()
        pct = self.hp / self.max_hp * 100

        if inimigo.mp == feitico.custo or feitico.tipo == "Magia Branca" and pct > 50:
            self.escolher_feitico_inimigo()
        else:
            return feitico, dano_magico
