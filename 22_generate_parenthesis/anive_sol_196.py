from itertools import combinations, product
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # create all possible combinations of the parenthesis
        # chcek each whether it's valid parenthesis or not
        # pattern = set([''.join(s) for s in  product('()', repeat=6)])
        pattern = [''.join(s) for s in  product('()', repeat=2*n)]
        # print(pattern)
        return getvalid(pattern)
        
def getvalid(pattern):
    valid_pattern = []
    for pat in pattern:
        stack = []
        isvalid = True
        for br in pat:
            if br == ')':
                if len(stack) == 0: 
                    isvalid = False
                    break
                top = stack.pop()
                if top != '(': 
                    isvalid = False 
                    break
            else:
                stack.append(br)
        if len(stack) == 0 and isvalid:
            valid_pattern.append(pat)
    return valid_pattern