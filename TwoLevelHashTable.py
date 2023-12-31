from tqdm import tqdm
from random import random, randint

MAXP = 655360001


class TwoLevelHashTable:
    def __init__(self, size):
        self.size = size
        self.keys = []
        self.values = []
        self.collision = 0
        self.primary_table = [None] * size

    def __len__(self) -> int:
        return self.size

    def load_words(self) -> list[str]:
        with open('english3.txt') as words_file:
            valid_words = set(words_file.read().split())
            self.keys = [key for key in valid_words if len(key) >= 3]
        return self.keys

    def get_values(self) -> list[int]:
        self.values = [int(random() * 100000) for _ in range(1, self.size)]
        return self.values

    def list_to_dict(self) -> dict:
        dict_words = dict(zip(self.load_words(), self.get_values()))
        return dict_words

    @staticmethod
    def get_hash_code(key) -> int:
        hc = 0
        characters = list(key)
        for character in characters:
            hc += ord(character)
        return hc

    @staticmethod
    def get_param():
        a = randint(1, MAXP - 1) % MAXP
        b = randint(1, MAXP) % MAXP
        return a, b

    def primary_hash(self, key, a, b) -> int:
        hc = self.get_hash_code(key)
        index = (a * hc + b) % MAXP % self.size
        return index

    def secondary_hash(self, key, a, b) -> int:
        hc = self.get_hash_code(key)
        index = (a * hc + b) % MAXP % self.size
        return index

    def insert(self, key, value):
        a, b = self.get_param()
        primary_index = self.primary_hash(key, a, b)
        if self.primary_table[primary_index] is None:
            self.primary_table[primary_index] = {}
        else:
            self.collision += 1
        secondary_table = self.primary_table[primary_index]

        a, b = self.get_param()
        secondary_index = self.secondary_hash(key, a, b)
        if secondary_table.get(secondary_index) is None:
            secondary_table[secondary_index] = {}

        secondary_table[secondary_index][key] = value


if __name__ == '__main__':
    my_size = 194205

    ht = TwoLevelHashTable(size=my_size)
    for k, v in tqdm(ht.list_to_dict().items()):
        ht.insert(k, v)
    print('Count of collisions after first hashing: ', ht.collision)
    print(f'After first hashing percent of collisions:  {ht.collision / len(ht) * 100:.2f}%')
    print(f'The total length of hash table is {len(ht)} key-value pairs')
