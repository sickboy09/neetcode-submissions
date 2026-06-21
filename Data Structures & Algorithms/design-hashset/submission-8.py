class MyHashSet:

    def __init__(self):
        self.maxl = 100
        self.hset = [[] for _ in range(self.maxl)]

    def add(self, key: int) -> None:
        index = key % self.maxl
        if key not in self.hset[index]:
            self.hset[index].append(key)

    def remove(self, key: int) -> None:
        index = key % self.maxl
        if key in self.hset[index]:
            self.hset[index].remove(key)

    def contains(self, key: int) -> bool:
        index = key % self.maxl
        return key in self.hset[index]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)