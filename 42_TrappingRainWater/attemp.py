def trap(height):
    l, r = 0, 1
    n = len(height)
    res = 0
    while r < n - 1:
        while r < n and height[l] > height[r]:
            r += 1
        if r == n:
            l += 1
        else:
            res += findArea(height[l:r+1])
            # print(height[l], height[r])
            l = r
        r = l + 1
    return res

def findArea(lst):
    n = len(lst)
    if n < 3:
        # too short valley
        return 0
    else:
        # calculate the trapped water here
        print(lst)
        return sum([lst[0] - a for a in lst[1:n-1]])

res = trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])

# res = trap([0,1,2,3,1,1,3])
print(res)
