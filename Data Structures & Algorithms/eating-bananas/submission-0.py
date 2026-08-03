class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, sum(piles)
        ans = 0
        def canEat(n):
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i]/n)
            
            return hours <= h
        while l <= r:
            m = (l + r) // 2
            if canEat(m):
                r = m - 1
                ans = m
            else:
                l = m + 1
        
        return ans