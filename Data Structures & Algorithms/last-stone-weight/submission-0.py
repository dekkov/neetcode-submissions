class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) >= 2:
            larger, smaller = heapq.heappop_max(stones), heapq.heappop_max(stones)
            if larger == smaller:
                continue
            else:
                heapq.heappush_max(stones, larger-smaller)
        
        return 0 if not stones else stones[0]