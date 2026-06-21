class MyHashMap:

    def __init__(self):
        self.maxl = 100
        self.hmap = [[] for _ in range(self.maxl)]

    def put(self, key: int, value: int) -> None:
        index = key % self.maxl
        for pair in self.hmap[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.hmap[index].append([key, value])

    def get(self, key: int) -> int:
        index = key % self.maxl
        for pair in self.hmap[index]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        index = key % self.maxl
        for pair in self.hmap[index]:
            if pair[0] == key:
                pair[1] = -1
                # self.hmap[index].remove(tup)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)