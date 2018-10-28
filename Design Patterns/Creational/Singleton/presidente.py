#Ensures that only one object of a particular class is ever created.

#There can only be one president of a country at a time. The same president has to be brought to action, whenever duty calls.
#President here is singleton.

class President:
    instance = None

    @classmethod
    def get_instance(cis):
        if not cls.instance:  #cls é sempre usada para o primeiro argumento de um metodo de uma classe
            cls.instance = President()
        return cls.instance

if __name__ == '__main__':

    president1 = President().get_instance()
    president2 = President().get_instance()
    assert president1 is president2
