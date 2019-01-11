from itertools import combinations, product
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # recursion approach
        if n==0:
            return []
        return gen_paran('', n, 0)

def gen_paran(s, op_available, num_unclosed):
    if op_available == 0:
        return [s+')'*num_unclosed]
    elif num_unclosed == 0:
        return gen_paran(s+'(', op_available - 1, num_unclosed + 1)
    return gen_paran(s+'(', op_available - 1, num_unclosed + 1) + gen_paran(s+')', op_available, num_unclosed - 1)