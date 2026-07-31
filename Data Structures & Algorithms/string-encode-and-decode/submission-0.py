class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string = string + str(len(s)) + "#" + s
        return string
    
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            size = int(s[i:j])
            ans.append(s[j+1:j+1+size])
            i = j + 1 + size
        return ans