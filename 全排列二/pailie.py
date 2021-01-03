import itertools

class Solution:
    def permuteUnique(self, nums):
        hash_num = dict()
        for item in nums:
            hash_num[item] = hash_num.get(item, 0) + 1
        output = []

        def backtrack(combination):
            if len(combination) == len(nums):
                output.append(combination)
            else:
                for num_key in list(hash_num.keys()):
                    hash_num[num_key] = hash_num.get(num_key, 0) - 1
                    # 当前数字已经用完, 从哈希表中删去该数字
                    if hash_num.get(num_key, 0) == 0:
                        hash_num.pop(num_key)
                    # 回溯搜索...
                    backtrack(combination + [num_key])
                    hash_num[num_key] = hash_num.get(num_key, 0) + 1
        backtrack([])
        return output

    def permuteUnique1(self, nums):
        return list(set(itertools.permutations(nums)))