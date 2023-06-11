class Stack:
    def __init__(self, stack):
        self.stack = []
        self.len = 0

    def print(self):
        if self.len == 0:
            return False
        else:
