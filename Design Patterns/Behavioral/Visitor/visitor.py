#Visitor pattern lets you add further operations to objects without having to modify them.

#Consider someone visiting Dubai. They just need a way (i.e. visa) to enter Dubai. After arrival,
#they can come and visit any place in Dubai on their own without having to ask for permission or to do some leg work in order to visit any place here;
#just let them know of a place and they can visit it. Visitor pattern lets you do just that,
#it helps you add places to visit so that they can visit as much as they can without having to do any legwork.

class Animal:

    def accept(operation):
        raise NotImplementedError

class AnimalOperation:

    def visit_monkey(monkey):
        raise NotImplementedError

    def visit_lion(lion):
        raise NotImplementedError

    def visit_dolphin(dolphin):
        raise NotImplementedError

class Monkey(Animal):

    def shout(self):
        print('Ooh oo aa aa!')

    def accept(self, operation):
        operation.visit_monkey(self)

class Lion(Animal):

    def roar(self):
        print('Roaaaaarr!')

    def accept(self, operation):
        operation.visit_lion(self)

class Dolphin(Animal):

    def speak(self):
        print('Tuut tuttu tuutt!')

    def accept(self, operation):
        operation.visit_dolphin(self)

class Speak(AnimalOperation):

    def visit_monkey(self, monkey):
        monkey.shout()

    def visit_lion(self, lion):
        lion.roar()

    def visit_dolphin(self, dolphin):
        dolphin.speak()

class Jump(AnimalOperation):

    def visit_monkey(self, monkey):
        print('Jumped 20 feet high! on the tree')

    def visit_lion(self, lion):
        print('Jumped 7 feet! back on the ground!')

    def visit_dolphin(self, dolphin):
        print('Walked on water a little and disappeared.')

if __name__ == '__main__':

    monkey = Monkey()
    lion = Lion()
    dolphin = dolphin()

    speak = Speak()
    jump = Jump()

    monkey.accept(speak)
    monkey.accept(jump)

    lion.accept(speak)
    lion.accept(jump)

    dolphin.accept(speak)
    dolphin.accept(jump)

    
