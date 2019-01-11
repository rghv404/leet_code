class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # this is what I;ve been waiting for
        if candidates is None or len(candidates) == 0:
            return []

        comb= []
        res = []
        candidates.sort()
        findComb(res, comb, candidates, target, 0)

        return res

def findComb(res, comb, candidates, target, start):
    if target == 0:
        # if comb not in res:
        res.append([a for a in comb])
        return

    for i in range(start, len(candidates)):
        if candidates[i] > target:
            break
        if i > start and candidates[i] == candidates[i-1]:
            continue
        comb.append(candidates[i])
        findComb(res, comb, candidates, target - candidates[i], i + 1)
        del comb[-1]

sol = Solution()
res = sol.combinationSum2([10,1,2,7,6,1,5], 8)
print(res)
