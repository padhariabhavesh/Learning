"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
"""


class RandomizedSet:

    def __init__(self):
        self.dictionary = {}
        self.count = 0

    def insert(self, val: int) -> bool:
        if self.dictionary.get(val) is None:
            self.dictionary[val] = 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if self.dictionary.get(val) is not None:
            self.dictionary.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        ran = [i for i in self.dictionary.keys()]
        return random.choice(ran)
