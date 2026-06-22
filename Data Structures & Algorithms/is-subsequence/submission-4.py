class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sl, tl = list(s), list(t)
        i = 0
        for j in range(len(t)):
            if i == len(sl):
                break
            if sl[i] == tl[j]:
                i += 1
        return i==len(s)

        