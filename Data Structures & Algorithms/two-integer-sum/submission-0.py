class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has = {}

        for i, num in enumerate(nums):
            look_for = target - num
            if look_for in has:
                return [has[look_for][0], i]
            else:
                if num in has:
                    has[num].append(i)
                else:
                    has[num] = [i]