class LinearProbeHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None for _ in range(size)]
        self.items = 0

    def insert(self, key, value):
        if self.items == self.size:
            print("Table full")
            return

        index = self._hash(key)
        # traverse the bucket in circular fashion
        while self.table[index] is not None:
            index = (index + 1) % self.size

        # empty spot found, insert here
        self.table[index] = (key, value)
        self.items += 1

    def search(self, key):
        index = self._hash(key)
        first_check = index
        # traverse the bucket in circular fashion
        while self.table[index] is not None:
            # match found
            if self.table[index][0] == key:
                return True
            index = (index + 1) % self.size
            # ensure not double-checking
            if index == first_check:
                return False

        return False

    def delete(self, key):
        index = self._hash(key)
        first_check = index
        item_deleted = False
        # traverse the bucket in circular fashion
        while self._table[index] is not None:
            if self._table[index][0] == key:
                self._table[index] = None
                item_deleted = True
                self.items -= 1
                break
            else:
                index = (index + 1) % self.size
                # ensure not double-checking
                if index == first_check:
                    print("Item not found")
                    return None
        if not item_deleted:
            print("Item not found")
            return
        # rehash elements in the primary bucket
        rehash_index = index + 1
        while self._table[rehash_index] is not None:
            entry = self._table[rehash_index]
            self._table[rehash_index] = None
            self.insert(entry[0], entry[1])
            rehash_index = (rehash_index + 1) % self.size

    def _hash(self, key):
        return int(key) % self.size
