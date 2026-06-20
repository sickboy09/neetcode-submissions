class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = len(nums)
        count = 0
        for i in range(l):
            if nums[i] == val:
                count += 1
        for i in range(count):
            nums.remove(val)
        return l-count
