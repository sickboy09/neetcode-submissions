class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] * (len(nums)+1)
        suff = [1] * (len(nums)+1)
        res = []
        for i in range(len(nums)):
            pref[i+1] = pref[i] * nums[i]
        for j in range(len(nums)-2, -1, -1):
            suff[j] = suff[j+1] * nums[j+1]
        for k in range(len(nums)):
            res.append(pref[k]*suff[k])
        return res
            