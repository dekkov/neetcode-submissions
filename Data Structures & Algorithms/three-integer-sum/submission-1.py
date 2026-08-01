class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums.sort()
        for i in range(len(nums) - 2):
            target = nums[i]
            if i > 0 and target == nums[i-1]:
                continue
            seen = set()
            for j in range(i+1, len(nums)):
                need = -(target + nums[j])
                if need in seen:
                    triplet = sorted([need, target, nums[j]])
                    if triplet not in ans:
                        ans.append(triplet)
                else:
                    seen.add(nums[j])
            
        return ans
