def function(lst):
    if lst is None:
        return []
    res = ''
    i = 0
    while i <= len(lst) - 1:
        occur = int(lst[i + 1])
        res += ''.join(lst[i] for j in range(occur))
        i += 2
    return res


res = function("i1s2b3h5j7")
print(res)
