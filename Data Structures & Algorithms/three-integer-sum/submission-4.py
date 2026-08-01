class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()


        def kSum(start, k, target):
            result = []

            # Not enough numbers remaining
            if len(nums) - start < k:
                return result

            # Base case: 2Sum
            if k == 2:
                left = start
                right = len(nums) - 1

                while left < right:
                    current_sum = nums[left] + nums[right]

                    if current_sum == target:
                        result.append([nums[left], nums[right]])

                        left += 1
                        right -= 1

                        # Skip duplicates
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1

                return result

            # Reduce kSum into (k - 1)Sum
            for i in range(start, len(nums) - k + 1):
                # Skip duplicate choices
                if i > start and nums[i] == nums[i - 1]:
                    continue

                smaller_results = kSum(
                    i + 1,
                    k - 1,
                    target - nums[i]
                )

                for combination in smaller_results:
                    result.append([nums[i]] + combination)

            return result

        return kSum(0, 3, 0)