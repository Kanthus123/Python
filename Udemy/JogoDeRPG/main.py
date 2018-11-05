import colorama #importante para usar cores no console do Windows - https://pypi.org/project/colorama/
import random
from colorama import Fore
from colorama import init
from classes.game import Pessoa, bcolors
from classes.magias import Feiticos
from classes.inventario import Item

init() #inicia colorama no Windows

print("\n\n")
#Criar Magia Negra
fire = Feiticos("Fire", 30, 600, "Magia Negra")
thunder = Feiticos("Thunder", 30, 600, "Magia Negra")
blizzard = Feiticos("Blizzard", 30, 600, "Magia Negra")
meteor = Feiticos("Meteor", 50, 1200, "Magia Negra")
quake = Feiticos("Quake", 45, 1500, "Magia Negra")

#Criar Magia Branca
cure = Feiticos("Cure", 27, 620, "Magia Branca")
cure2 = Feiticos("Cure 2", 34, 2000, "Magia Branca")

# Cria Item
pocao_pequena = Item("Poção Pequena", "poção", "Cura 50 HP", 50)
pocao_media = Item("Poção Média", "poção", "Cura 100 HP", 100)
pocao_grande = Item("Poção Grande", "poção", "Cura 150 HP", 150)
elixir = Item("Elixir", "elixir", "Cura completamente o HP/MP de um membro do grupo", 9999)
elixir_grande = Item("Elixir Grande", "elixir", "Cura completamente o HP/MP de todos os membros do grupo", 9999)

granada = Item("Granada", "ataque", "Da 500 pontos de dano", 500)

magias_jogador = [fire, thunder, blizzard, meteor, cure, cure2]
itens_jogador = [{"item": pocao_pequena, "quantidade": 5}, {"item": pocao_media, "quantidade": 5},
                 {"item": pocao_grande, "quantidade": 5}, {"item": elixir, "quantidade": 5},
                 {"item": elixir_grande, "quantidade": 5}, {"item": granada, "quantidade": 5}]

#Instancia Pessoa
jogador1 = Pessoa("Kanthus", 3250, 132, 300, 34, magias_jogador, itens_jogador)
jogador2 = Pessoa("Kelthor", 4150, 188, 311, 34, magias_jogador, itens_jogador)
jogador3 = Pessoa("Seforas", 3050, 150, 288, 34, magias_jogador, itens_jogador)
inimigo = Pessoa("Tiamat", 12200, 700, 500, 25, [], [])

jogadores = [jogador1, jogador2, jogador3]

running  = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "UM INIMIGO ATACA!!" + bcolors.ENDC)

while running: #funciona enquanto a batalha estiver ocorrendo
    print("=========================================")

    print("\n")
    print("NOME                       HP                                      MP")

    for jogador in jogadores:
        jogador.get_status()

    print("\n")
    inimigo.get_status_inimigo()

    for jogador in jogadores:
        jogador.escolher_acao()
        escolha = input("Escolha uma Opção: ")
        index = int(escolha) - 1
        print("Você escolheu:", escolha)

        if index  == 0: #Dano Fisico
            dmg = jogador.gerar_dano()
            inimigo.receber_dano(dmg)
            print("Você deu:", dmg, "pontos de dano fisico no inimigo.")
        elif index == 1: #Dano Magico
            jogador.escolher_magia()
            escolha_magia = int(input("Escolha uma magia:")) - 1
            if escolha_magia == -1:
                continue
            feitico = jogador.magia[escolha_magia]
            dano_magico = feitico.gerar_dano_magico()

            mp_atual = jogador.get_mp()

            if feitico.custo > mp_atual:
                print(bcolors.FAIL + "\nVocê não tem mana o suficiente!\n" + bcolors.ENDC)
                continue
            jogador.reduzir_mp(feitico.custo)

            if feitico.tipo == "Magia Branca":
                jogador.curar(dano_magico)
                print(bcolors.OKBLUE + "\n" + feitico.nome + " lhe curou em", dano_magico, " pontos de HP." + bcolors.ENDC)
            elif feitico.tipo == "Magia Negra":
                inimigo.receber_dano(dano_magico)
                print(bcolors.OKBLUE + "\n" + feitico.nome + " causa ", dano_magico, " de pontos de dano." + bcolors.ENDC)
        elif index == 2:
            jogador.escolher_itens()
            item_escolha = int(input("Qual item deseja usar? ")) - 1

            if item_escolha == -1:
                continue

            item = jogador.itens[item_escolha]["item"]
            jogador.itens[item_escolha]["quantidade"] -= 1

            if jogador.itens[item_escolha]["quantidade"] == 0:
                print(bcolors.FAIL + "\n" + "o item acabou...." + bcolors.ENDC)
                continue

            if item.tipo == "poção":
                jogador.curar(item.prop)
                print(bcolors.OKGREEN + "\n" + item.nome + " cura em ", item.prop, " pontos de HP." + bcolors.ENDC)
            elif item.tipo == "elixir":

                if item.name == "Elixir Grande":
                    for i in jogadores:
                        i.hp = i.max_hp
                        i.mp = i.max_mp
                else:
                    jogador.hp = jogador.max_hp
                    jogador.mp = jogador.max_mp

                print(bcolors.OKGREEN + "\n" + item.nome + " HP/MP completamente restaurados" + bcolors.ENDC)
            elif item.tipo == "ataque":
                inimigo.receber_dano(item.prop)
                print(bcolors.OKGREEN + "\n" + item.nome + " causa", item.prop, " pontos de dano." + bcolors.ENDC)

    inimigo_escolha = 1
    alvo = random.randrange(0, 3)
    inimigo_dmg = inimigo.gerar_dano()
    jogadores[alvo].receber_dano(inimigo_dmg)
    print(bcolors.FAIL + "Você recebeu:", inimigo_dmg, "pontos de dano do inimigo. HP atual:", jogador.get_hp(), bcolors.ENDC)

    if inimigo.get_hp() == 0: #Checagem de vitoria ou derrota
        print(bcolors.OKGREEN + "Você venceu!!!" + bcolors.ENDC)
        running = False
    elif jogador.get_hp() == 0:
        print(bcolors.FAIL + "Você foi derrotado pelo inimigo !!!!" + bcolors.ENDC)
        running = False
