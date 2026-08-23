class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        cur = []
        def backtrack(i):
            if i >= len(nums):
                ans.add(tuple(sorted(cur.copy())))
                return
            
            cur.append(nums[i])
            backtrack(i+1)
            cur.pop()

            backtrack(i+1)

        backtrack(0)
        res = [_ for _ in ans]
        return res