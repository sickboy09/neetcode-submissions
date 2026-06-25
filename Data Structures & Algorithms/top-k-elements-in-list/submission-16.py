class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        bucket = [[] for _ in range(len(nums)+1)]
        for key, val in Counter(nums).items():
            bucket[val].append(key)
        for buc in bucket[::-1]:
            l = len(buc)
            while l > 0 and k > 0:
                res.append(buc[l-1])
                l -= 1
                k -= 1
        return res



