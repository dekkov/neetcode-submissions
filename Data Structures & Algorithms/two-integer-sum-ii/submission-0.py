class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        seen = {} #value:index

        for i,n in enumerate(numbers):
            need = target - n
            if need in seen:
                return [seen[need]+1, i+1]
            
            else:
                seen[n] = i
        
        return [0,0]