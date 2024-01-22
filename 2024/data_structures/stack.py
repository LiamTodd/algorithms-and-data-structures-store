class ArrayStack:
    MAX_LENGTH = 10000

    def __init__(self, items):
        self.top = 0
        self.stack = [None for _ in range(ArrayStack.MAX_LENGTH)]
        for item in items:
            self.push(item)

    def is_full(self):
        return self.top == ArrayStack.MAX_LENGTH

    def is_empty(self):
        return self.top == 0

    def push(self, item):
        if self.is_full():
            raise ValueError("Stack is full.")
        self.stack[self.top] = item
        self.top += 1

    def pop(self):
        if self.is_empty:
            raise ValueError("Stack is empty.")
        item = self.stack[self.top - 1]
        self.top -= 1
        return item


class LinkedListStack:
    pass
