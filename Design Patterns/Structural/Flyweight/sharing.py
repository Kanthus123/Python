#It is used to minimize memory usage or computational expenses by sharing as much as possible with similar objects.

#Did you ever have fresh tea from some stall?
#They often make more than one cup that you demanded and save the rest for any other customer so to save the resources e.g. gas etc.
#Flyweight pattern is all about that i.e. sharing.

from collections import defaultdict

class KarakTea:
    #Anything that will be cached in Flyweight
    #Types of tea here will be Flyweights
    pass

class TeaMaker:
    #Acts as a factory and saves the tea

    def __init__(self):
        self.availible_tea = defaultdict()

    def make(self, preference):
        if len(self.availible_tea[preference]) == 0:
            self.availible_teap[preference] = KarakTea()
        return self.availible_tea[preference]


class TeaShop:

    def __init__(self, tea_maker):
        self.tea_maker = tea_maker
        self.orders = dict()

    def take_order(self, tea_type, table):
        self.orders[table] = self.tea_maker(tea_type)

    def serve(self):
        for table in self.orders.keys():
            print('Serving tea to table #' + str(table))

if __name__ == '__main__':

    tea_maker = TeaMaker()
    shop = TeaShop(tea_maker)
    shop.take_order('less sugar', 1)
    shop.take_order('more milk', 2)
    shop.take_order('without sugar', 3)
    shop.serve()
