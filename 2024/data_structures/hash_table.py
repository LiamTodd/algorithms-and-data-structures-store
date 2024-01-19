class LinearProbeHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None for _ in range(size)]

    def insert(self, key, value):
        index = self._hash(key)
        first_check = index
        # traverse the bucket in circular fashion
        while self.table[index] is not None:
            index = (index + 1) % self.size
            # ensure table is not full
            if index == first_check:
                print("Table full")
                return None

        # empty spot found, insert here
        self.table[index] = (key, value)

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
        # linear probe from index
        # empty cell when found
        # look forward from bucket, checking hash values of keys
        # look for the end of the bucket, move that value into the empty spot
        pass

    def _hash(self, key):
        return int(key) % self.size
