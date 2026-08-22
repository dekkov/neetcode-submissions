class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []

        def backtrack(i, total):
            if total == target:
                ans.append(cur.copy())
                return
            if i == len(nums) or total > target:
                return
            
            backtrack(i+1, total)
            cur.append(nums[i])
            backtrack(i, total + nums[i])
            cur.pop()
        
        backtrack(0, 0)
        return ans