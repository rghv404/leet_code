# from itertools import product
# class Solution:
#     def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """
#         d_ = {1: '*', 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz', 0:' '}
#         strs = []
#         if not digits:
#             return []
#         for d in digits:
#             strs.append(d_[int(d)])
#         return [''.join(item) for item in product(*strs)]
#

def letterCombinations(digits):
    if not digits:
        return []

    d_ = {1: '*', 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz', 0:' '}

    def get_combination(res, comb, index):
        if len(comb) == len(digits):
            res.append(comb)
            return
        for c in d_[int(digits[index])]:
            print(c)
            get_combination(res, comb + c, index + 1)
    res = []
    get_combination(res, '', 0)
    return res


print(letterCombinations('23'))
