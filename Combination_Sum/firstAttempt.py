def combinationSum(candidates, target):
    stack = []
    res = []
    j = 0
    if target in candidates:
        res.append([target])
        candidates.remove(target)
    candidates.sort()
    for i in range(len(candidates)):
        stack = []
        while sum(stack) < target:
            stack.append(candidates[i])
        print(stack)
        k = i
        print(k)
        while len(stack) >= 1:
            print('Inside second while loop')
            while sum(stack) < target:
                stack.append(candidates[k])
            print(stack)
            if sum(stack) == target:
                res.append([a for a in stack])
                print('We\'ve got some result', res)
            del stack[-1]
            index = candidates.index(stack[-1])
            del stack[-1]
            print(stack)
            if k < len(candidates) - 1:
                k = index + 1
    print(res)

# combinationSum([2,3,6,7], 7)
# combinationSum([8,7,4,3], 11)
combinationSum([7,3], 17)
