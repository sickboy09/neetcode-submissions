class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        max_el = None
        res = []
        for i in range(k):
            maximum = 0
            for key in counter:
                if counter[key] > maximum:
                    max_el = key 
                    maximum = counter[max_el]
            res.append(max_el)
            del counter[max_el]
        return res



