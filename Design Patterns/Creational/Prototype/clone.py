#Create object based on an existing object through cloning.

#Remember dolly? The sheep that was cloned! Lets not get into the details but the key point here is that it is all about cloning

#The prototype pattern is a creational design pattern in software development.
#It is used when the type of objects to create is determined by a prototypical instance,
#which is cloned to produce new objects.

import copy

class Sheep:

    def __init__(self, nome, categoria='Carneiro-selvagem'):
        self.nome = nome
        self.categoria = categoria

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_categoria(self, categoria):
        self.categoria = categoria

    def get_categoria(self):
        return self.categoria

if __name__ == '__main__':

    original = Ovelha('Jolly')
    assert original.get_nome() == 'Jolly'
    assert original.get_categoria() == 'Carneiro-selvagem'

    clonado = copy.deepcopy(original)
    clonado.set_nome('Dolly')
    assert clonado.get_nome() == 'Dolly'
    assert clonado.get_categoria() == 'Carneiro-selvagem'
