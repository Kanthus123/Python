#Every organization is composed of employees.
#Each of the employees has the same features i.e.
#has a salary, has some responsibilities,
#may or may not report to someone,
#may or may not have some subordinates etc.

#Composite pattern lets clients treat the individual objects in a uniform manner.

class Empregado:

    def get_nome(self):
        raise NotImplementedError

    def set_salario(self, salario):
        raise NotImplementedError

    def get_salario(self):
        raise NotImplementedError

    def get_funcao(self):
        raise NotImplementedError

class Desenvolvedor(Empregado):

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_nome(self):
        return self.nome

    def set_salario(self, salario):
        self.salario = salario

    def get_salario(self):
        return self.salario

    def get_funcao(self):
        return self.funcao

class Designer(Empregado):

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_nome(self):
        return self.nome

    def set_salario(self, salario):
        self.salario = salario

    def get_salario(self):
        return self.salario

    def get_funcao(self):
        return self.funcao

class Organizacao:

    def __init__(self):
        self.empregados = [ ]

    def add_empregado(self, empregado):
        self.empregados.append(empregado)

    def get_net_salarios(slef):
        net_salario = 0
        for empregado in self.empregados:
            net_salario += empregado.get_salario()
        return net_salario

if __name__ == '__main__':

    john = Desenvolvedor('John Doe', 120000)
    jane = Designer('Jane Doe', 100000)
    organizacao = Organizacao()
    organizacao.add_empregado(john)
    organizacao.add_empregado(jane)
    assert organizacao.get_net_salarios == 220000
