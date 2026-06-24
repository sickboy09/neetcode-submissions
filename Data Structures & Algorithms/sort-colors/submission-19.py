class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l = len(nums)
        i, j, k = 0, l-1, 0

        while k <= j:
            if nums[k] == 0:
                self.swap(i, k, nums)
                k += 1
                i += 1
            elif nums[k] == 2:
                self.swap(j, k, nums)
                j -= 1
            else:
                k += 1
        
    def swap(self, a, b, nums):
        nums[a], nums[b] = nums[b], nums[a]