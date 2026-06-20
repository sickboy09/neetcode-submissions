class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        n = int(len(nums)/2)
        for num in nums:
            hm[num] = 1 + hm.get(num, 0)

        for num in hm:
            if hm[num] >= n:
                return num