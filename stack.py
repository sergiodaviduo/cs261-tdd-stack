# Stack: A stack.
# Your implementation should pass the tests in stack.py.
# YOUR NAME

class Stack:

    data = None

    def is_empty(self):
        if self.data == None:
            return True
        else:
            return False

    def pop(self):
        if self.is_empty() == True:
            try:
                a = [1,2]
                # I think this is cheating but......
                a[-100]
            except IndexError as e:
                raise IndexError('index out of range.')

        popdata = None
        for x in self.data:
            popdata = x

        self.data.remove(popdata)

        return popdata

    def peek(self):
        if self.is_empty() == True:
            try:
                a = [1,2]
                # I think this is cheating but......
                a[-100]
            except IndexError as e:
                raise IndexError('index out of range.')
        peekdata = None
        for x in self.data:
            peekdata = x

        return peekdata

    def push(self, val):
        if self.data == None:
            self.data = []
        self.data.append(val)

    pass
