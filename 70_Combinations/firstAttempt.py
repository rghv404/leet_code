def combine(n, k):
    if n is None or k > n:
        return []
    if k == n:
        if k == 0:
            return [[]]
        return [[a for a in range(1, n+1)]]
    res = []
    comb = []
    findComb(res, n, comb, k, 1)
    return res

def findComb(res, n, comb, k, start):
    if len(comb) == k:
        res.append(comb[:])
        return
    for i in range(start, n+1):
        comb.append(i)
        findComb(res, n, comb, k, i+1)
        del comb[-1]

res = combine(78,2)
print(res)
