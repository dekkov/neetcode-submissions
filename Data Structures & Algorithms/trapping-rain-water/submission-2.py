class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]
        ans = 0
        """
        Why move the side with the smaller maximum? Assume left_max <= right_max:

1. left_max is the bottleneck, so the water at the current left position is fully determined by left_max.

2. We already know there is a right wall at least as tall as right_max, and right_max >= left_max. Therefore, changing the right side cannot increase the water at the current left position.

3. If height[left] is greater than left_max, it becomes the new left_max and traps 0 water at that position.

4. Otherwise, the trapped water is:
   left_max - height[left]

5. Then we move left because the water at that position has been finalized.
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


