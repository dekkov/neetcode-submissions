class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]
        ans = 0
        """
        Why we only shift whatever side that has max smaller (left for example):
        1. That is our bottle neck, left max is smaller so if we move right max, the number of water still depends on smaller max
        2. What if we encounter a max bigger than right max, no worries, we wouldn't be able to add any water as it the highest wall.
        3. => we can add water later when shifting later
        """
        while l < r: 
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                ans += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                ans += maxRight - height[r]
        
        return ans


