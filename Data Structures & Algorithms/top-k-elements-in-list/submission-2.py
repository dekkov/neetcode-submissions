class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        heap = []

        for key,v in freq.items():
            heapq.heappush(heap, (v,key))
        
        for i in range(len(heap) - k):
            heapq.heappop(heap)
        
        return [e2 for (e1,e2) in heap]