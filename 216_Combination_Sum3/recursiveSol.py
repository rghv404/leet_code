def combinationSum_3(k, n):
    if k == 0:
        if n == 0:
            return [[]]
        return

    res = []
    comb = []
    findComb(res, comb, k , n, 1)
    return res

def findComb(res, comb, k, target, start):
    # base case when the length and target is achived
    if len(comb) == k and target == 0:
        res.append(comb[:])
        return
    for i in range(start, 10):
        if i > target:
            break
        comb.append(i)
        findComb(res, comb, k, target - i, i + 1)
        comb.pop()

res = combinationSum_3(3, 1)
print(res)
