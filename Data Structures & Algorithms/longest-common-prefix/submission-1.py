class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = len(strs)
        len_array = [len(x) for x in strs]
        smallest = sorted(len_array)[0]
        prefix = ""

        for i in range(smallest):
            present_in = 0
            for st in strs:
                if strs[0][i] == st[i]: 
                    present_in += 1
            if present_in == l:
                prefix += strs[0][i]
            elif i == 0:
                return prefix

        return prefix
        