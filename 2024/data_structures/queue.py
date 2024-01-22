class ArrayQueue:
    MAX_SIZE = 10000

    def __init__(self, items):
        self.back = 0
        self.front = 0
        self.length = 0
        self.queue = [None for _ in range(ArrayQueue.MAX_SIZE)]
        for item in items:
            self.append(item)

    def append(self, item):
        if self.is_full():
            raise ValueError("Queue is full.")
        self.queue[self.back] = item
        self.back = (self.back + 1) % ArrayQueue.MAX_SIZE
        self.length += 1

    def serve(self):
        if self.is_empty():
            raise ValueError("Queue is empty.")
        item = self.queue[self.front]
        self.front = (self.front + 1) % ArrayQueue.MAX_SIZE
        self.length -= 1
        return item

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == ArrayQueue.MAX_SIZE


class LinkedListQueue:
    pass
