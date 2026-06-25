class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        max_el = None
        res = []
        for i in range(k):
            maximum = 0
            for k in counter:
                if counter[k] > maximum:
                    max_el = k 
                    maximum = counter[max_el]
            res.append(max_el)
            del counter[max_el]
        return res



