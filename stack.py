#Implementação de uma pilha

class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        data self.stack[-1]
        return data

    def sizeStack(self):
        return len(self.stack)
