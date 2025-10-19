# from collections import defaultdict
#
# class Solution:
#     def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#
#         result = defaultdict(list)
#
#         for s in strs:
#             SortedS = ''.join(sorted(s))
#             result[SortedS].append(s)
#         return list(result.values())

# d = {}
# d["a"].append(1)
# print(d)

def groupAnagrams(words):
    groups = {}

    for word in words:
        count = [0] * 26

        for char in word:
            index = ord(char) - ord("a")
            count[index] = count[index] + 1

        key = tuple(count)

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())








