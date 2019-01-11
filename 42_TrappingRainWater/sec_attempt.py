def trap(height):
    n = len(height)
    l, r = 0, n-1
    res = 0
    while l < n:
        while l < r - 1:
            # print(height[l:r])
            if all(a < height[l] and a < height[r] and a is not None for a in height[l+1:r]):
                # print('We\'re in')
                # print(height[l:r+1], l, r)
                res += findArea(height[l:r+1])
                l = r - 1
                break
            else:
                r -= 1
        l += 1
        r = n-1
    print(res)

def findArea(lst):
    n = len(lst)
    if n < 3:
        return 0
    item = lst[0] if lst[0] < lst[n-1] else lst[n-1]
    # print(lst[1:n-1], item)
    return sum([item - a for a in lst[1:n-1]])

trap([0,7,1,4,6])
trap([4,4,4,7,1,0])
trap([0,1,0,2,1,0,1,3,2,1,2,1])
