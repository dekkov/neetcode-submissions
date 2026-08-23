class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = set()
        cur = []
        def backtrack(i, total):
            if total == target:
                ans.add(tuple(cur.copy()))
                return

            if total > target or i >= len(candidates):
                return
            
            val = candidates[i]
            cur.append(val)
            backtrack(i+1, total+val)
            cur.pop()
            while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            backtrack(i+1, total)
        backtrack(0,0)
        
        res = [list(_) for _ in ans]
        return res