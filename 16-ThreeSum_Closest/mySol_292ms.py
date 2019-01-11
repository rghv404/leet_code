from bisect import bisect_left
from collections import defaultdict


def distinct(a, b, num, d_):
    if num == b and num == a and d_[b] > 2:
        return True
    elif num == a and num != b and d_[a] > 1:
        return True
    elif num == b and num != a and d_[b] > 1:
        return True
    elif num != a and num != b:
        return True
    return False


def nearest(myList, myNumber):
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return myList[0]
    if pos == len(myList):
        return myList[-1]
    before = myList[pos - 1]
    after = myList[pos]
    if after - myNumber < myNumber - before:
        return after
    else:
        return before


class Solution:

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # store in a dicitonry to check the dsistincntess in o(n) time
        nums.sort()
        d_ = defaultdict(int)
        n = len(nums)
        for a in nums:
            d_[a] += 1
        # print(d_)
        gap = float("infinity")
        for i in range(n - 1):
            # l2 = [k for k in nums if k != nums[i]]
            for j in range(i + 1, n):
                a, b = nums[i], nums[j]
                ideal = target - (a + b)
                if ideal in d_ and distinct(a, b, ideal, d_):
                    return target
                else:
                    # removing first occurences of a and b so they are not sent back as closest,
                    # easiest method i could think of
                    # l2.remove(b)
                    # print(l2)
                    # find closest to ideal candidate
                    closest = nearest(nums, ideal)
                    # print('Closes for iteration {0}-{1} where a:{2} and b:{3} is {4}'.format(i, j, a, b,closest))
                    if not distinct(a, b, closest, d_):
                        break
                    sum_ = a + b + closest
                    if abs(target - sum_) < gap:
                        gap = abs(target - sum_)
                        closest_sum = sum_
                    # print('Closest sum for iteration {0}-{1} where a:{2} and b:{3} is {4}'.format(i, j, a, b, closest_sum))
        return closest_sum
            
