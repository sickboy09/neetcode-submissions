class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l = len(nums)
        i, j, k = 0, l-1, 0
            
        for i in range(l):
            for j in range(l-1):
                if nums[j+1] < nums[j]:
                    nums[j], nums[j+1] = nums[j+1], nums[j] 

        