from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for index1 in range (n):
            for index2 in range ( index1 + 1, n):
                if nums[index1] + nums[index2] == target:
                    return [index1, index2]
        return None

result = Solution()
Solution.twoSum([2,3,4,5], 5)