class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        stack = []
        ans = []
        for n in nums:
            if n < 0:
                stack.append(n)
                continue
            else:
                while stack and n >= -1 * stack[-1]:
                    num = stack.pop()
                    ans.append(num * num)
                ans.append(n * n)
        
        while stack:
            num = stack.pop()
            ans.append(num * num)

        return ans