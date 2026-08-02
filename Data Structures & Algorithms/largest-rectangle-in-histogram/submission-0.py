class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        [7,1,7,2,2,4] - use value here for better visualization
        1. fill in the stack with (value, index)
        2. We need to keep it monotonic increasing
            -> if val < stack[-1][0]:
            -> cal it, pop it and replace with (val, stack[-1][1])
        """
        stack = [] #(value,index)
        ans = 0
        for i, v in enumerate(heights):
            start_i = i  
            while stack and stack[-1][0] > v:
                height, prev_i = stack.pop()
                ans = max(ans, height*(i-prev_i))
                start_i = prev_i

            stack.append([v,start_i])
        
        for height, prev_i in stack:
            ans = max(ans, height * (len(heights) - prev_i))
        return ans

