import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []  # (-value, index)
        ans = []
        l = 0

        for r in range(len(nums)):
            heapq.heappush_max(maxHeap, (nums[r], r))

            if r - l + 1 > k:
                l += 1

            # Remove elements outside the current window
            while maxHeap[0][1] < l:
                heapq.heappop_max(maxHeap)

            if r - l + 1 == k:
                ans.append(maxHeap[0][0])

        return ans