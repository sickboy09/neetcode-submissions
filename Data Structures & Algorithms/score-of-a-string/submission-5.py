class Solution:
    def scoreOfString(self, s: str) -> int:
        ord_dict = {x:ord(x) for x in s}
        sum = 0
        for i in range(len(s)-1):
            sum += abs(ord_dict[s[i]] - ord_dict[s[i+1]])
        return sum