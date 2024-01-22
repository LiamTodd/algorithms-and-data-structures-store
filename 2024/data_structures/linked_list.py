class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def link(self, node):
        self.next = node

    def unlink(self):
        self.next = None


class LinkedList:
    def __init__(self, elements: []):
        self.length = 0
        self.head = None
        self.tail = None
        if len(elements) == 0:
            return
        # head = tail initially
        self.head = LinkedListNode(elements[0])
        self.tail = self.head
        self.length = 1
        # append elements
        for element in elements[1:]:
            self.append(element)

    def append(self, value):
        new_node = LinkedListNode(value)
        if self.is_empty():
            # special case: list is empty: set the head
            self.head = new_node
        else:
            # otherwise, connect new node to old tail
            self.tail.next = new_node
        # update tail
        self.tail = new_node
        self.length += 1

    def insert_at_index(self, index, value):
        if index < 0 or index >= self.length:
            raise IndexError("Invalid index.")

        # special case: insert at the end is the same as append
        if index == self.length - 1:
            self.append(value)
        else:
            new_node = LinkedListNode(value)
            # special case: insert at index 0 - replace head
            if index == 0:
                new_node.next = self.head
                self.head = new_node
            else:
                current = self.head
                j = 0
                while j < index - 1:
                    current = current.next
                    j += 1
                # current is at index-1.
                new_node.next = current.next
                current.next = new_node

            self.length += 1

    def is_empty(self):
        return self.length == 0

    def get_length(self):
        return self.length

    def get_tail(self):
        return self.tail

    def get_head(self):
        return self.head

    def delete(self, index):
        if index < 0 or index >= self.length:
            raise IndexError(f"Index {index} out of range. Length={self.length}")

        current = self.head
        previous = None

        # special case: delete head
        if index == 0:
            # reassign the head
            self.head = current.next
        else:
            j = 0
            while j < index:
                previous = current
                current = current.next
                j += 1
            # 'skip' the deleted item
            previous.next = current.next

        # special case: delete tail
        if index == self.length - 1:
            self.tail = previous

        self.length -= 1

    def get_at_index(self, index):
        if index < 0 or index >= self.length:
            raise IndexError(f"Index {index} out of range. Length={self.length}")
        current = self.head
        j = 0
        while j < index:
            current = current.next
            j += 1
        return current.value

    def search(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        raise ValueError("value not in list.")

    def to_list(self):
        l = []
        current = self.head
        while current is not None:
            l.append(current.value)
            current = current.next
        return l


if __name__ == "__main__":
    print("Test initialisation")
    ll = LinkedList([1, 2, 3, 4, 5, 6, 7, 8])
    print(ll.get_head().value)
    print(ll.get_tail().value)
    print(ll.get_length())
    print(ll.search(1))
    print(ll.search(2))
    print(ll.search(7))
    print(ll.search(8))
    try:
        ll.search(0)
        print("something went wrong")
    except ValueError:
        pass

    print("Test delete")
    print(ll.to_list())
    try:
        ll.delete(-1)
        print("something went wrong")
    except IndexError:
        pass
    try:
        ll.delete(ll.get_length())
        print("something went wrong")
    except IndexError:
        pass

    # delete head
    print(ll.to_list())
    print(ll.get_head().value)
    ll.delete(0)
    print(ll.to_list())
    print(ll.get_length())
    print(ll.get_head().value)

    # delete head again
    print(ll.to_list())
    print(ll.get_head().value)
    ll.delete(0)
    print(ll.to_list())
    print(ll.get_length())
    print(ll.get_head().value)

    # delete non-head
    print(ll.to_list())
    ll.delete(1)
    print(ll.to_list())
    print(ll.get_length())

    # delete tail
    print(ll.to_list())
    ll.delete(ll.get_length() - 1)
    print(ll.to_list())
    print(ll.get_tail().value)

    print("Test empty list")
    ll = LinkedList([])
    print(ll.to_list())
    print(ll.get_head())
    print(ll.get_tail())
    print(ll.get_length())

    print("Test length 1 list")
    ll = LinkedList([99])
    print(ll.to_list())
    print(ll.get_head().value)
    print(ll.get_tail().value)
    print(ll.get_length())
    print(ll.search(99))
    print(ll.get_at_index(0))
    ll.delete(0)
    print(ll.get_head())
    print(ll.get_tail())
    print(ll.get_length())
    print(ll.to_list())

    print("Test insert at index")
    ll = LinkedList([1, 2, 3])
    ll.insert_at_index(0, "zero")
    print(ll.to_list())
    print(ll.get_head().value)
    ll.insert_at_index(ll.get_length() - 1, "end")
    print(ll.to_list())
    print(ll.get_length())
    print(ll.get_tail().value)

    ll.insert_at_index(2, "middle")
    print(ll.to_list())
    print(ll.get_length())
