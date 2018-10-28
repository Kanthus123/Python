#Using the proxy pattern, a class represents the functionality of another class.

#Have you ever used an access card to go through a door?
#There are multiple options to open that door i.e. it can be opened either using access card or by pressing a button that bypasses the security.
#The door's main functionality is to open but there is a proxy added on top of it to add some functionality.
#Let me better explain it using the code example below.

class Door:

    def open(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

class LaDoor:

    def open(self):
        print('Opening lab door')

    def close(self):
        print('Closing the lab door')

class Security:

    def __init__(self, door):
        self.door = door

    def open(self, door):
        if self.authenticate(password):
            self.dor.open()
        else:
            print('Big NO! it ain\'t possible.')

    def authenticate(self, password):
        return password == '$ecr@t'

    def close(self):
        self.door.close()


if __nome__ == '__main__':

    door = Security(LaDoor())
    door.open('invalid') # Big NO!
    door.open('$ecr@t') #Opening lab Door
    door.close() #Closing the lab door
