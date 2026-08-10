class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x1, x2):
            return math.sqrt((x1) ** 2 + (x2) ** 2)
        heap = [] #maxHeap
        for i, j in points:
            d = distance(i,j)
            heapq.heappush_max(heap, [d, [i,j]])

            if len(heap) > k:
                heapq.heappop_max(heap)
        ans = []
        for _, p in heap:
            ans.append(p)
        return ans