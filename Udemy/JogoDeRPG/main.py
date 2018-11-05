import colorama #importante para usar cores no console do Windows - https://pypi.org/project/colorama/
from colorama import Fore
from colorama import init
from classes.game import Pessoa, bcolors
from classes.magias import Feiticos
from classes.inventario import Item

init() #inicia colorama no Windows

print("\n\n")
#Criar Magia Negra
fire = Feiticos("Fire", 10, 100, "Magia Negra")
thunder = Feiticos("Thunder", 10, 100, "Magia Negra")
blizzard = Feiticos("Blizzard", 10, 100, "Magia Negra")
meteor = Feiticos("Meteor", 20, 200, "Magia Negra")
quake = Feiticos("Quake", 15, 150, "Magia Negra")

#Criar Magia Branca
cure = Feiticos("Cure", 12, 120, "Magia Branca")
cure2 = Feiticos("Cure 2", 18, 200, "Magia Branca")

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
jogador1 = Pessoa("Kanthus", 450, 65, 60, 34, magias_jogador, itens_jogador)
jogador2 = Pessoa("Kelthor", 450, 65, 60, 34, magias_jogador, itens_jogador)
jogador3 = Pessoa("Seforas", 450, 65, 60, 34, magias_jogador, itens_jogador)
inimigo = Pessoa("Tiamat", 1200, 65, 45, 25, [], [])

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
                print(bcolors.BLUE + "\n" + feitico.nome + " curado em", dano_magico, " pontos de HP." + bcolors.ENDC)
            elif feitico.tipo == "Magia Negra":
                inimigo.receber_dano(dano_magico)
                print(bcolors.BLUE + "\n" + feitico.nome + " causa ", dano_magico, " de pontos de dano." + bcolors.ENDC)
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
                jogador.hp = jogador.max_hp
                jogador.mp = jogador.max_mp
                print(bcolors.OKGREEN + "\n" + item.nome + " HP/MP completamente restaurados" + bcolors.ENDC)
            elif item.tipo == "ataque":
                inimigo.receber_dano(item.prop)
                print(bcolors.OKGREEN + "\n" + item.nome + " causa", item.prop, " pontos de dano." + bcolors.ENDC)

    inimigo_escolha = 1

    inimigo_dmg = inimigo.gerar_dano()
    jogador1.receber_dano(inimigo_dmg)
    print(bcolors.FAIL + "Você recebeu:", inimigo_dmg, "pontos de dano do inimigo. HP atual:", jogador.get_hp(), bcolors.ENDC)

    print("=========================================") #Resultados dos ataques
    print("HP atual do inimigo:", bcolors.FAIL + str(inimigo.get_hp()) + "/" + str(inimigo.get_max_hp()) + bcolors.ENDC)
    print("MP atual do inimigo", bcolors.OKBLUE + str(inimigo.get_mp()) + "/" + str(inimigo.get_max_mp()) + bcolors.ENDC)

    if inimigo.get_hp() == 0: #Checagem de vitoria ou derrota
        print(bcolors.OKGREEN + "Você venceu!!!" + bcolors.ENDC)
        running = False
    elif jogador.get_hp() == 0:
        print(bcolors.FAIL + "Você foi derrotado pelo inimigo !!!!" + bcolors.ENDC)
        running = False
