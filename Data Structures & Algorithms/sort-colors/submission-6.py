class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l = len(nums)           
        for i in range(l):
            swapped = False
            for j in range(l-1):
                if nums[j+1] < nums[j]:
                    nums[j], nums[j+1] = nums[j+1], nums[j] 
                    swapped = True
            if swapped == False:
                return

        