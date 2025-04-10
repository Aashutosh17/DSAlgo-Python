from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closets = nums[0]

        for x in nums:
            if abs(x)< abs(closets):
                closets = x

        if closets < 0 and abs(closets) in nums:
            return abs(closets)
        else:
            return closets
