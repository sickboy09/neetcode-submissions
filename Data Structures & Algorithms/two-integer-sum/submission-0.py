class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range(l):
            req = target - nums[i]
            for j in range(l):
                if nums[j] == req and i != j:
                    return [i, j]
        

        