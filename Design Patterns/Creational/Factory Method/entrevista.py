#Provem uma manira de delgar instanciações logicas para as classes filho

class Entrevista:

    @staticmethod
    def fazer_pergunta():
        NotImplementedError



class Desenvolvedor(Entrevista):

    def fazer_pergunta(self):
        print('Perguntar sobre Design Patterns')

class Executivo(Entrevista):

    def fazer_pergunta(self):
        print("Perguntar sobre construções para a comunidade")

class EmpregarGerente:

    def fazer_entrevista(self):
        raise NotImplementedError

    def escolher_pergunta(self):
        entrevista = self.fazer_entrevista()
        entrevista.criar_pergunta()

class GerenteDeDesenvolvimento(EmpregarGerente):
    def fazer_entrevista(self):
        return Desenvolvedor()

class GerenteDeMarketing(EmpregarGerente):
    def fazer_entrevista():
        return Executivo()


if __name__ == '__main__':

    dev_gerente = GerenteDeDesenvolvimento()
    dev_gerente.fazer_entrevista()

    mkt_gerente = GerenteDeMarketing()
    mkt_gerente.fazer_entrevista()
