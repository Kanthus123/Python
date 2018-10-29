#It lets you change the behavior of a class when the state changes.

#Imagine you are using some drawing application, you choose the paint brush to draw.
#Now the brush changes its behavior based on the selected color i.e. if you have chosen red color it will draw in red,
#if blue then it will be in blue etc.

class WritingState:

    def write(self, words):
        raise NotImplementedError

class UpperCase(WritingState):

    def write(self, words):
        print(words.upper())

class LowerCase(WritingState):

    def write(self, words):
        print(words.lower())

class Default(WritingState):
    print(words)

class TextEditor:

    def __init__(self, state):
        self.state = state

    def set_state(self, state):
        self.state = state

    def type(self, words):
        self.state.write(words)

if __name__ == '__main__':

    editor = TextEditor(Default())
    editor.type('First Line')

    editor.set_state(UpperCase())
    editor.type('Second Line')
    editor.type('Third Line')

    editor.set_state(LowerCase())
    editor.type('Fourth Line')
    editor.type('Fifth line')
