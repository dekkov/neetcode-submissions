from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums) #num:freq
        freq_bucket = [[] for n in range(len(nums)+1)]
        
        for num, freq in freq_map.items():
            freq_bucket[freq].append(num)
        
        ans = []
        for i in range(len(freq_bucket)-1, -1, -1):
            if freq_bucket[i]:
                for j in range(len(freq_bucket[i]) - 1, -1, -1):
                    ans.append(freq_bucket[i][j])
                    k -= 1
            if k <= 0:
                return ans