class Solution:
    def firstUniqChar(self, s: str) -> int:
        bag = dict()
        for i in s:
            bag[i] = bag.get(i, 0) + 1
        for ind, i in enumerate(s):
            if bag[i] == 1:
                return ind
        return -1