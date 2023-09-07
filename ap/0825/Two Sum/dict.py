from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, n in enumerate(nums):
            nums_map[n] = i

        # 타겟에서 첫 번재 수를 뺀 결과를 키로 조회
        for i, n in enumerate(nums):
            complement = target - n
            if complement in nums_map and i != nums_map[complement]:
                return [i, nums_map[complement]]


nums = [2, 7, 11, 15]
target = 9
# nums = [3, 2, 4]
# target = 6
# nums = [3, 3]
# target = 6

solution = Solution()
print(solution.twoSum(nums, target))