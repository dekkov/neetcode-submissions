class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        max_q = deque()
        l = 0

        for r in range(len(nums)):
            while max_q and max_q[-1] < nums[r]:
                max_q.pop()
            
            max_q.append(nums[r])


            if r + 1 >= k:
                res.append(max_q[0])
                if max_q[0] == nums[l]:
                    max_q.popleft()
                l += 1
        
        return res
    

        