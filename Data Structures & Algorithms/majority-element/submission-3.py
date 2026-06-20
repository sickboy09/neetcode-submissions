class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        n = len(nums)//2
        for num in nums:
            hm[num] = 1 + hm.get(num, 0)
            if hm[num] > n:
                return num