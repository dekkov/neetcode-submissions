class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # formula: time = (target - position) / speed
        """
        1. Calculate time to reach target for each car sorted by destinations
        2. 
        """

        cars = sorted(zip(position, speed))
        times = [float(target - p) / s for p, s in cars]
        ans = 0

        lead = 0
        for t in reversed(times):
            if t > lead:
                ans += 1
                lead = t
        
        return ans

        



        