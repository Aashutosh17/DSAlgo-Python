class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, n in enumerate(nums):
            needed_number = target - n
            if needed_number in seen:
                return [seen[needed_number], i]
            else: seen[n] = i



