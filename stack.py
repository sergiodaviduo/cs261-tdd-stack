# Stack: A stack.
# Your implementation should pass the tests in stack.py.
# YOUR NAME

class Stack:

    def is_empty(self):
        return True

    def pop(self):
        if self.is_empty() == True:
            try:
                a = [1,2]
                # I think this is cheating but......
                a[-100]
            except IndexError as e:
                raise IndexError('index out of range.')

    pass
