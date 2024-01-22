class BinaryTreeHeap:
    MAX_SIZE = 10000

    def __init__(self, items):
        self.next_available_index = 0
        self.heap = [None for _ in range(BinaryTreeHeap.MAX_SIZE)]
        for item in items:
            self.insert(item)

    def is_empty(self):
        return self.heap[0] is None

    def is_full(self):
        return self.next_available_index == BinaryTreeHeap.MAX_SIZE

    def insert(self, item):
        if self.is_full():
            raise ValueError("Heap is full.")

        # add element to bottom level of the heap
        index = self.next_available_index
        parent_index = (index - 1) // 2
        self.heap[index] = item
        # compare element to its parent (if it has one). If it is smaller than the parent, stop
        while index > 0 and self.heap[index] > self.heap[parent_index]:
            # else, swap the element and its parent and repeat
            self.heap[index] = self.heap[parent_index]
            self.heap[parent_index] = item
            index = (index - 1) // 2
            parent_index = (index - 1) // 2

        # update next available index
        self.next_available_index += 1

    def pop_max(self):
        if self.is_empty():
            raise ValueError("Heap is empty.")

        # replace the root (store it somewhere) of the heap with the last element on the last level
        max_value = self.heap[0]
        self.heap[0] = self.heap[self.next_available_index - 1]
        self.heap[self.next_available_index - 1] = None

        sink_index = 0
        left_child_index = sink_index * 2 + 1
        right_child_index = sink_index * 2 + 2
        # compare the new root with its children. If it is larger than its children, stop
        while (
            self.heap[left_child_index] is not None
            and self.heap[sink_index] < self.heap[left_child_index]
        ) or (
            self.heap[right_child_index] is not None
            and self.heap[sink_index] < self.heap[right_child_index]
        ):
            # else, swap the element with the larger of its children and repeat
            if (
                self.heap[right_child_index] is None
                or self.heap[left_child_index] > self.heap[right_child_index]
            ):
                # left is larger, so swap with left OR there is no right child
                left_child_value = self.heap[left_child_index]
                self.heap[left_child_index] = self.heap[sink_index]
                self.heap[sink_index] = left_child_value
                sink_index = left_child_index
            else:
                # right is larger, so swap with right
                right_child_value = self.heap[right_child_index]
                self.heap[right_child_index] = self.heap[sink_index]
                self.heap[sink_index] = right_child_value
                sink_index = right_child_index

            # update child indexes
            left_child_index = sink_index * 2 + 1
            right_child_index = sink_index * 2 + 2

        self.next_available_index -= 1
        return max_value

    def peek(self):
        # return value of root (without removing it)
        if self.is_empty():
            raise ValueError("Heap is empty.")
        return self.heap[0]


if __name__ == "__main__":
    items = [100, 2, 7, 3, 17, 19, 1, 36, 25]
    heap = BinaryTreeHeap(items)
    print(heap.heap[: len(items)])
    print([i for i in range(len(items))])

    print(heap.peek())

    print(heap.pop_max())
    print(heap.heap[: len(items)])
    print([i for i in range(len(items))])
    print(heap.peek())

    for _ in range(len(items)):
        print(heap.heap[: len(items)])
        print(heap.pop_max())
