class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        buckets = [[] for _ in range(len(nums)+1)]
        for key, val in Counter(nums).items():
            buckets[val].append(key)
        for bucket in reversed(buckets):
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res


