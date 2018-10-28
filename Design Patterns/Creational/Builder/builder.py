#Allows you to create different flavors of an object while avoiding constructor pollution. Useful when there could be several flavors of an object. Or when there are a lot of steps involved in creation of an object.

#Imagine you are at Hardee's and you order a specific deal, lets say,
#{}"Big Hardee" and they hand it over to you without any questions;
#this is the example of simple factory.
#But there are cases when the creation logic might involve more steps.
#For example you want a customized Subway deal,
#you have several options in how your burger is made e.g what bread do you want? what types of sauces would you like? What cheese would you want? etc. In such cases builder pattern comes to the rescue.

class Burger:

    def __init__(self, builder):
        self.size = builder.size
        self.cheese = builder.cheese
        self.pepperoni = builder.pepperoni
        self.lettuce = builder.lettuce
        self.tomato = builder.tomato

class BurgerBuilder:

    def __init__(self, size):
        self.size = size
        self.cheese = False
        self.pepperoni = False
        self.lettuce = False
        self.tomato = False

    def add_cheese(self):
        self.cheese = True

    def add_pepperoni(self):
        self.pepperoni = True

    def add_lettuce(self):
        self.lettuce = True

    def add_tomato(self):
        self.tomato = tomato

    def build(self):
        return Burger(self)

if __name__ == '__main__':

    burger = BurgerBuilder(6)
    burger.add_cheese()
    burger.add_lettuce()
    burger.build()
