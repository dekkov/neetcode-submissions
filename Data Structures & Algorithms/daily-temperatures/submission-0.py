class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)

        stack = [] # indices

        for i in range(len(temperatures)):
            temp = temperatures[i]
            
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                ans[index] = i - index

            stack.append(i)
        
        return ans

