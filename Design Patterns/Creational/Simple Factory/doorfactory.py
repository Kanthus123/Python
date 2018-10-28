#Simple Factory simplesmete gera uma instancia para um cliente sem expor qualquer tipo de instanciação logica para o cliente

#Exemplo: Considere que voce quer contruir uma casa e você precisa de portas. Você pode ttanto colocar suas roupas de carpinteiro,
#pegar um pouco de madeira, cola, pregos e ferrametnas para construir a porta da sua casa ou simplismente ligar para a fabrica # -*- coding: utf-8 -*-
#pedir para eles fazerem a porta e entregarem pra você e com isso você não precisa aprender nada sobre como contruir uma porta.

class Door:
    def GetWidth(self):
        print("Largura")
    def GetHeight(self):
        print("Altura")

class WoodenDoor(Door):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

class DoorFactory:

    @staticmethod
    def make_door(width, height):
        return WoodenDoor(width, height)


if __name__ == '__main__':

    door = DoorFactory().make_door(100,200)

    assert door.get_width() == 100
    assert door.get_height() == 200
