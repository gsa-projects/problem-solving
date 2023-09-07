from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n
            if complement in nums[i + 1:]:
                return [i, nums[i + 1:].index(complement) + i + 1]


nums = [2, 7, 11, 15]
target = 9
# nums = [3, 2, 4]
# target = 6

solution = Solution()
print(solution.twoSum(nums, target))