class Solution:
    def scoreOfString(self, s: str) -> int:
        ord_list = [ord(x) for x in s]
        sum = 0
        for i in range(len(s)-1):
            diff = abs(ord_list[i] - ord_list[i+1])
            sum += diff
        return sum