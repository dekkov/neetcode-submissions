class Solution:
    def trap(self, height: List[int]) -> int:

        maxHeight = 0
        ans = 0
        walls = [0] * len(height)
        for i in range(len(height)):
            maxHeight = max(maxHeight, height[i])
            walls[i] = maxHeight
        
        maxHeight = 0
        for i in range(len(height) - 1, -1, -1):
            maxHeight = max(maxHeight, height[i])
            walls[i] = min(walls[i], maxHeight)

        for i in range(len(walls)):
            ans += walls[i] - height[i]
        
        return ans

