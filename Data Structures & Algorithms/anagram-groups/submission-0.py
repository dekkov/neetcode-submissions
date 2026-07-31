from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list) #tuple of chars: str list
        
        chars = [0] * 26
        for s in strs:
            copy = chars.copy()
            for c in s:
                copy[ord(c) - ord('a')] += 1
            hashMap[tuple(copy)].append(s)
        
        ans = []
        for val in hashMap.values():
            ans.append(val)
        return ans