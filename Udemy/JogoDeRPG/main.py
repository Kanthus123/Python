import colorama
from colorama import Fore
from colorama import init
from classes.game import Pessoa, bcolors

init() #inicia colorama no Windows

magias = [{"nome": "Fire", "custo": 10, "dmg": 60},
         {"nome": "Thunder", "custo": 10, "dmg": 80},
         {"nome": "Blizzard", "custo": 10, "dmg": 60}]

jogador = Pessoa(450, 65, 60, 34, magias)
inimigo = Pessoa(1200, 65, 45, 25, magias)

running  = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "UM INIMIGO ATACA!!" + bcolors.ENDC)

while running:
    print("=========================================")
    jogador.escolher_acao()
    escolha = input("Escolha uma Opção: ")
    index = int(escolha) - 1

    print("Você escolheu:", escolha)

    if index  == 0:
        dmg = jogador.gerar_dano()
        inimigo.receber_dano(dmg)
        print("Você deu:", dmg, "pontos de dano fisico no inimigo.")
    elif index == 1:
        jogador.escolher_magia()
        escolha_magia = int(input("Escolha uma magia:")) - 1
        dano_magico = jogador.gerar_dano_feitico(escolha_magia)
        feitico = jogador.get_nome_feitico(escolha_magia)
        custo = jogador.get_custo_feitico(escolha_magia)

        mp_atual = jogador.get_mp()

        if custo > mp_atual:
            print(bcolors.FAIL + "\nVocê não tem mana o suficiente!\n" + bcolors.ENDC)
            continue

        jogador.reduzir_mp(custo)
        inimigo.receber_dano(dano_magico)
        print(bcolors.OKBLUE + "\nVocê deu:", dano_magico, "pontos de magico no inimigo com:", feitico, "!!!" + bcolors.ENDC)


    inimigo_escolha = 1

    inimigo_dmg = inimigo.gerar_dano()
    jogador.receber_dano(inimigo_dmg)
    print(bcolors.FAIL + "Você recebeu:", inimigo_dmg, "pontos de dano do inimigo. HP atual:", jogador.get_hp(), bcolors.ENDC)

    print("=========================================")
    print("HP atual:", bcolors.OKGREEN + str(jogador.get_hp()) + "/" + str(jogador.get_max_hp()) + bcolors.ENDC)
    print("MP atual:", bcolors.OKBLUE + str(jogador.get_mp()) + "/" + str(jogador.get_max_mp()) + bcolors.ENDC + "\n")

    print("HP atual do inimigo:", bcolors.FAIL + str(inimigo.get_hp()) + "/" + str(inimigo.get_max_hp()) + bcolors.ENDC)
    print("MP atual do inimigo", bcolors.OKBLUE + str(inimigo.get_mp()) + "/" + str(inimigo.get_max_mp()) + bcolors.ENDC)

    if inimigo.get_hp() == 0:
        print(bcolors.OKGREEN + "Você venceu!!!" + bcolors.ENDC)
        running = False
    elif jogador.get_hp() == 0:
        print(bcolors.FAIL + "Você foi derrotado pelo inimigo !!!!" + bcolors.ENDC)
        running = False
