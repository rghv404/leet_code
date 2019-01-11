def combinationSum(candidates, target):
    if candidates is None or len(candidates) == 0:
        return []
    res = []
    comb = set()
    candidates.sort()
    findComb(res, comb, candidates, target, 0)
    print(res)


def findComb(res, comb, candidates, target, start):
    # print('The f')
    if target == 0:
        res.append([a for a in comb])
        return
    for i in range(start, len(candidates)):
        if candidates[i] > target:
            break
        comb.append(candidates[i])
        findComb(res, comb, candidates, target - candidates[i], i + 1)
        del comb[-1]


# combinationSum([3, 7], 17)
# combinationSum([3,4,7,8], 11)
# combinationSum([2,3,6,7], 7)
combinationSum([1, 2, 3, 4, 7], 7)
