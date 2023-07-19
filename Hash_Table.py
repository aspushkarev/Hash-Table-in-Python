class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def __len__(self) -> int:
        return self.size

    def __contains__(self, key) -> bool:
        try:
            self.search(key)
            return True
        except KeyError:
            return False

    def is_contains(self, key) -> bool:
        try:
            self.search(key)
            return True
        except KeyError:
            return False

    @staticmethod
    def get_hash_code(key) -> int:
        """ метод получает хэш-код """
        hc = 0
        characters = list(key)
        for character in characters:
            hc += ord(character)
        return hc

    def get_hash(self, hash_code) -> int:
        """ метод получает хэш-значение """
        return int(hash_code % self.capacity)

    def get_index(self, key) -> int:
        """ метод получает индекс """
        hash_code = self.get_hash_code(key)
        index = self.get_hash(hash_code)
        return index

    def insert(self, key, value):
        """ метод вставляет пару ключ-значение """
        index = self.get_index(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def search(self, key):
        """ метод ищет значение по ключу """
        index = self.get_index(key)

        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(key)

    def remove(self, key):
        """ метод удаляет пару ключ-значение """
        index = self.get_index(key)

        previous = None
        current = self.table[index]
        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next
        raise KeyError(key)


if __name__ == '__main__':
    ht = HashTable()

    ht.insert('bananas', 23)
    ht.insert('apple', 2)
    ht.insert('fruits', 34)

    print('apple' in ht)
    print('box' in ht)
    print(ht.is_contains('fruits'))

    print(len(ht))
