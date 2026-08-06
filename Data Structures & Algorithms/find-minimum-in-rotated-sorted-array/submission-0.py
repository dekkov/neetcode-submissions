class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        [3,4,5,6,1,2]
        [6,1,2,3,4,5]
        """
        l, r = 0, len(nums) - 1
        ans = 10000
        while l <= r:
            mid = (l+r) // 2
            ans = min(ans, nums[mid])

            if nums[mid] < nums[-1]:
                r = mid - 1
            
            else:
                l = mid + 1
        return ans


