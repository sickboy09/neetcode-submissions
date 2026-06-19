class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range(l):
            req = target - nums[i]
            for j in range(i+1, l):
                if nums[j] == req:
                    return [i, j]
        return []

        