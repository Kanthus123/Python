#Bridge pattern is about preferring composition over inheritance. Implementation details are pushed from a hierarchy to another object with a separate hierarchy.

#Consider you have a website with different pages and you are supposed to allow the user to change the theme.
#What would you do? Create multiple copies of each of the pages for each of the themes
#or would you just create separate theme and load them based on the user's preferences?
#Bridge pattern allows you to do the second i.e.

class WebPage:

    def get_conteudo(self):
        raise NotImplementedError

class About(WebPage):

    def __init__(self, tema):
        self.tema = tema

    def get_conteudo(self):
        return 'Pagina about em  ' = self.tema.get_cor()

class Carreiras(WebPage):

    def __init__(self, tema):
        self.tema = tema

    def get_conteudo(self):
        return 'Pagina carreiras em ' = self.tema.get_cor()

class Tema:

    def get_cor(self):
        pass

class TemaEscuro(Tema):

    def get_cor(self):
        return 'Dark Black'

class TemaClaro(Tema):

    def get_cor(self):
        return 'Off White'

class TemaAzul(tema):

    def get_cor(self):
        return 'Light Blue'

if __name__ == '__main__':

    tema_escuro = TemaEscuro()
    about = About(tema_escuro)
    carreiras = Carreiras(tema_escuro)
    assert about.get_conteudo() == 'Pagina About em Dark Black'
    assert about.get_conteudo() == 'Pagina Carreiras em Dark Black'
