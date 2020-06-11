'''
Random Pick with Weight

Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

    1 <= w.length <= 10000
    1 <= w[i] <= 10^5
    pickIndex will be called at most 10000 times.

Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]

Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.

'''
import random
class Solution:

    def __init__(self, w: [int]):
        self.indexLst = []
        for num in w:
            self.indexLst.extend([i for i in range(num)])
        
        self.alreadyPicked = []

    def pickIndex(self) -> int:
        randInd = random.randint(0, len(self.indexLst)-1)
        print(self.indexLst)
        while randInd in self.alreadyPicked: 
            randInd = random.randint(0, len(self.indexLst)-1)

        self.alreadyPicked.append(randInd)

        return self.indexLst[randInd]

class SolutionTwo:

    def __init__(self, w: [int]):
        self.weightSums = []
        weight = 0
        for num in w:
            weight += num
            self.weightSums.append(weight)
        
    def pickIndex(self) -> int:
        # randInd = random.randint(self.weightSums[0], self.weightSums[-1]) # not a true random int
        randPre = random.random() * self.weightSums[-1] # this give float more generalzied
        # for i, num in enumerate(self.weightSums):
        #     if randPre < num:
        #         return i
        # instead of linear saerch we can also do a bianry search because of the sorted prefix sum array
        l, r = 0, len(self.weightSums) - 1
        while l < r:
            mid = (l+r)//2
            if self.weightSums[mid] < randPre: l = mid + 1
            else: r = mid
        # if exact not found then it means l var denotes it's supposesd position
        return l

arr = [1,3,5,6]
obj = SolutionTwo(arr)
print(obj.pickIndex(), obj.pickIndex(), obj.pickIndex(), obj.pickIndex(), obj.pickIndex())