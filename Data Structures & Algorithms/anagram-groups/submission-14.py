class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret_lst = []
        for i in range(len(strs)):
            if strs[i] is None:
                continue
            grp = [strs[i]]
            for j in range(i+1, len(strs)):
                if strs[j] is None:
                    continue
                if Counter(strs[i]) == Counter(strs[j]):
                    grp.append(strs[j])
                    strs[j] = None
            ret_lst.append(grp)
        return ret_lst
