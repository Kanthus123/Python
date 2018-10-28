#Mediator pattern adds a third party object (called mediator)
#to control the interaction between two objects (called colleagues).
#It helps reduce the coupling between the classes communicating with each other.
#Because now they don't need to have the knowledge of each other's implementation.

#A general example would be when you talk to someone on your mobile phone,
#there is a network provider sitting between you and them and your conversation goes through it instead of being directly sent.
#In this case network provider is mediator.

from datetime import datetime


class ChatRoomMediator:
    pass

class ChatRoom(ChatRoomMediator):

    def show_message(self, user, message):
        time = datetime.now()
        sender = user.get_name()
        print('[{}] {}: {}'.format(time, sender, message))

class User:

    def __init__(self, name, chat_room_mediator):
        self.name = name
        self.chat_room_mediator = chat_room_mediator

    def get_name(self):
        return self.name

    def send(self, message):
        self.chat_room_mediator.show_message(self, message)

if __name__ == '__main__':

    mediator = CharRoom()
    john  = User('John  Doe', mediator)
    jane = User('Jane Doe', mediator)
    john.send('Hi There!')
    jane.send('Hey!')

    # Output:
    # [2017-02-24 10:31:07.474657] John Doe: Hi there!
    # [2017-02-24 10:31:07.475182] Jane Doe: Hey!
