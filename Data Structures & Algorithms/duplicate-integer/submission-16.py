class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        return False if sorted(nums) == sorted(list(nums_set)) else True
        
        