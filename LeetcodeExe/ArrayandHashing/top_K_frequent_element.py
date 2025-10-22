class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {} # a dict to count how many times each number appears

        for n in nums:
            count[n] = count.get(n,0) + 1

        # make a frequency bucket
        freq = [[] for i in range(len(nums)+1)]
        # We created a list of empty list

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range (len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res
