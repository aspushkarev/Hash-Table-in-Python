# pip install random-word
# pip install tqdm
from random_word import RandomWords
from tqdm import tqdm
import random


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.collision = 0
        self.table = [None] * capacity

    def __len__(self) -> int:
        return self.size

    def __contains__(self, key) -> bool:
        try:
            self.search(key)
            return True
        except KeyError:
            return False

    def __str__(self) -> str:
        elements = []
        for i in range(self.capacity):
            current = self.table[i]
            while current:
                elements.append((current.key, current.value))
                current = current.next
        return str(elements)

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
                    self.collision += 1
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

    @staticmethod
    def get_word():
        """ метод генерации случайных слов """
        r = RandomWords()
        return r.get_random_word()

    def fill_ht(self):
        """ метод наполнения хеш-таблицы """
        for _ in tqdm(range(self.capacity - self.size)):
            key = ht.get_word()
            value = random.randint(1, self.capacity)
            self.insert(key, value)


if __name__ == '__main__':
    ht = HashTable(10)

    ht.insert('bananas', 23)
    ht.insert('apple', 2)
    ht.insert('fruits', 34)

    print('My hash table:\n', ht)
    print('Is \'apple\' in hash table?:\n', 'apple' in ht)
    print('Is \'box\' in hash table?:\n', 'box' in ht)
    print('Is \'fruits\' in hash table?:\n', ht.is_contains('fruits'))
    print('The length of hash table:\n', len(ht))

    print('Filling hash table...Please wait')
    ht.fill_ht()
    print('My hash table:\n', ht)
    print('The length of hash table:\n', len(ht))
    print('Count of collisions:\n', ht.collision)

    print('Added \'fruits\' into hash table.')
    ht.insert('fruits', 3333)
    print('My hash table:\n', ht)
    print('The length of hash table:\n', len(ht))
    print('Count of collisions:\n', ht.collision)

    # Test on collision
    ht.insert('pencil', 8)
    ht.insert('cat', 49)
    ht.insert('man', 15)
    print('My hash table:\n', ht)
    print('The length of hash table:\n', len(ht))
    print('Count of collisions:\n', ht.collision)
