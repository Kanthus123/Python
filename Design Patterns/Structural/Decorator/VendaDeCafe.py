#Decorator pattern lets you dynamically change the behavior of an object at run time by wrapping them in an object of a decorator class.

#Imagine you run a car service shop offering multiple services.
#Now how do you calculate the bill to be charged?
#You pick one service and dynamically keep adding to it the prices for the provided services till you get the final cost.
#Here each type of service is a decorator.

class Cofe:

    def get_custo(self):
        raise NotImplementedError

    def get_descricao(self):
        raise NotImplementedError

class CafeSimples(Cafe):

    def get_custo(self):
        return 10

    def get_descricao(self):
        return 'Cafe Simples'

class CafeComLeite(self):

    def __init__(self, cafe):
        self.cafe = cafe

    def get_custo(self):
        return self.cafe.get_custo() + 2

    def get_descricao(self):
        return self.cafe.get_descricao() + ', leite'

class CafeComCreme(Cafe):

    def __init__(self, cafe):
        self.cafe = cafe

    def get_custo(self):
        return self.cafe.get_custo() + 5

    def get_descricao(self):
        return self.cafe.get_descricao() + ', creme'

class Capuccino(Cafe):

    def __init__(self, cafe):
        self.cafe = cafe

    def get_custo(self):
        return self.cafe.get_custo() + 3

    def get_descricao(self):
        return self.cafe.get_descricao() + ', chocolate'

if __name__ == '__main__':

    cafe = CafeSimples()
    assert cafe.get_custo() == 10
    assert coffee.get_description() == 'Cafe Simples'

    cafe = CafeComLeite(cafe)
    assert coffee.get_cost() == 12
    assert coffee.get_description() == 'Cafe Simples, Leite'

    cafe = CafeComCreme(cafe)
    assert coffee.get_cost() == 17
    assert coffee.get_description() == 'Cafe Simples, Leite, Creme'

    cafe = Capuccino(cafe)
    assert coffee.get_cost() == 20
    assert coffee.get_description() == 'Cafe Simples, Leite, Chocolate'
