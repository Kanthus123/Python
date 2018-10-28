#A factory of factories; a factory that groups the individual but related/dependent factories together without specifying their concrete classes.

#Extending our door example from Simple Factory.
#Based on your needs you might get a wooden door from a wooden door shop,
#iron door from an iron shop or a PVC door from the relevant shop.
#Plus you might need a guy with different kind of specialities to fit the door,
#for example a carpenter for wooden door, welder for iron door etc.
#As you can see there is a dependency between the doors now,
#wooden door needs carpenter, iron door needs a welder etc.

class Door:

    def get_descricao(self):
        raise NotImplementedError

class WoodenDoor(Door):

    def get_descricao(self):
        print('Eu sou uma porta de Madeira')

def IronDoor(Door):

    def get_descricao(self):
        print('Eu sou uma porta de Ferro')

class DoorFittingExpert:

    def get_descricao(self):
        raise NotImplementedError

class Welder(DoorFittingExpert):

    def get_descricao(self):
        print('Eu apenas posso colocar portas de ferro')

class Carpenter(DoorFittingExpert):

    def get_descricao(self):
        print('Eu apenas posso colocar portas de madeira')

class DoorFactory:

    def fazer_porta(self):
        raise NotImplementedError

    def fazer_profissional(self):
        raise NotImplementedError

class WoodenDoorFactory(DoorFactory):

    def fazer_porta(self):
        return WoodenDoor()

    def fazer_profissional(self):
        return Carpenter()

class IronDoorFactory(DoorFactory):

    def fazer_porta(self):
        return IronDoor()

    def fazer_profissional(self):
        return Welder()

if __name__ == '__main__':

    wooden_factory = WoodenDoorFactory()
    porta = wooden_factory.fazer_porta()
    profissional = wooden_factory.fazer_profissional()
    porta.get_descricao()
    profissional.get_descricao()

    iron_factory = IronDoorFactory()
    porta = iron_factory.fazer_porta()
    profissional = iron_factory.fazer_profissional()
    porta.get_descricao()
    profissional.get_descricao()
    
