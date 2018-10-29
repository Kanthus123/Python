#Template method defines the skeleton of how a certain algorithm could be performed, but defers the implementation of those steps to the children classes.

#    Suppose we are getting some house built. The steps for building might look like

#        Prepare the base of house
#        Build the walls
#        Add roof
#        Add other floors

#    The order of these steps could never be changed i.e. you can't build the roof before building the walls etc but each of the steps could be modified for example walls can be made of wood or polyester or stone.

class Builder:

    def build(self):
        raise NotImplementedError

    def lint(self):
        raise NotImplementedError

    def assemble(self):
        raise NotImplementedError

    def deploy(self):
        raise NotImplementedError

class AndroidBuilder(Builder):

    def test(self):
        print('Running Android tests')

    def lint(self):
        print('Linting the Android code')

    def assemble(self):
        print('Assembling the Android Builde')

    def deploy(self):
        print('Deplaying Android build to server')

class IosBuilder(Builder):

    def test(self):
        print('Running IOS tests')

    def lint(self):
        print('Linting the IOS code')

    def assemble(self):
        print('Assembling the IOS Builde')

    def deploy(self):
        print('Deplaying Android build to server')

if __name__ == '__main__':

    android_builder = AndroidBuilder()
    android_builder.build()

    ios_builder = IosBuilder()
    ios_builder.build()
    
