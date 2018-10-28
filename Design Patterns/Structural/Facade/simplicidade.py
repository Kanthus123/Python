#Facade pattern provides a simplified interface to a complex subsystem

#How do you turn on the computer? "Hit the power button" you say!
#That is what you believe because you are using a simple interface that computer provides on the outside,
#internally it has to do a lot of stuff to make it happen.
#This simple interface to the complex subsystem is a facade.


class Computer:

    def get_eletric_shock(self):
        print('Ouch')

    def make_sound(self):
        print('Beep Beep')

    def show_loading_screen(self):
        print('Loading...')

    def bam(self):
        print('Ready to be used')

    def clone_everything(self):
        print('Bup bup bup buzzzz!')

    def sooth(self):
        print('Haaaah!')

class ComputerFacade:

    def __init__(self, computer):
        self.computer = computer

    def turn_on(self):
        self.computer.get_eletric_shock()
        self.computer.make_sound()
        self.computer.show_loading_screen()
        self.computer.bam()

    def turn_off(self):
        self.computer.close_everything()
        self.computer.pull_current()
        self.computer.sooth()

if __name__ == '__main__':

    computer = ComputerFacade(Computer())

    computer.turn_on()

    computer.turn_off()
