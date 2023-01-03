
from ast import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = collections.defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            ana[tuple(count)].append(s)

        return ana.values()
        