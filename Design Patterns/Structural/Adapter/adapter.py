class Leao:

    def roar(self):
        raise NotImplementedError

class LeaoAfricano(Leao):

    def rugido():
        pass

class LeaoAsiatico(Leao):

    def rugido():
        pass

class Hunter:

    def hunt(self, leao):
        pass

class CachorroSelvagem:

    def latido(self):
        pass

#Adapta o Cachorro Selvagem para ser compativel com o programa
class CachorroSelvagemAdapter(Leao):

    def __init__(self, cachorro):
        self.cachorro = cachorro

    def rugido(self):
        self.cachorro.latido()

if __name__ == '__main__':

    cachorro_selvagem = CachorroSelvagem()
    cachorro_selvagem_adapter = CachorroSelvagemAdapter(cachorro_selvagem)
    hunter = Hunter()
    hunter.hunt(cachorro_selvagem_adapter)
