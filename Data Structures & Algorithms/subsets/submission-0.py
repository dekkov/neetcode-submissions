class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        for i, n in enumerate(nums):
            temp = []
            for ss in ans:
                copy = ss.copy()
                copy.append(n)
                temp.append(copy)
            for ss in temp:
                ans.append(ss)
        return ans

        
