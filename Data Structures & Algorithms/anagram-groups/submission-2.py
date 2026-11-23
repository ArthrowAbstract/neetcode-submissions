from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == [""]:
            return [[""]]
        d = {}
        for i in strs:
            t = hash(tuple(sorted(tuple(i))))
            if t in d: d[t].append(i)
            else:
                d[t] = [i]
        return list(d.values())
        