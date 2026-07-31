class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        def dfs(i, j):
            if i == len(t):
                return 1
            if j == len(s):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            
            res = dfs(i,j+1)
            if t[i] == s[j]:
                res  += dfs(i+1, j+1) 
            dp[(i,j)] = res
            return res
        return dfs(0,0)