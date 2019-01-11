def trap(height):
    l, r = 0, len(height) - 1
    l_max, r_max = 0, 0
    ans = 0
    # we start from both ends, initially max pillars on both left and right sides are 0
    while l < r:
        # we check which pillar is larger on both ends
        if height[l] < height[r]:
            # if left pillar is smaller than right, then we enter this loop
            # we check if the left pillar is left max, we do this to see if the
            # current pillar will hold any water or it'll overflow
            if height[l] >= l_max:
                l_max = height[l]
            else:
            # if the left pillar is smaller than left max then we calcualte the
            # store water and then subtract it from the l_max
                ans += l_max - height[l]
            l += 1
        else:
            # logic similar to above is used here, but from the rgight perspective
            if height[r] >= r_max:
                r_max = height[r]
            else:
                ans += r_max - height[r]
            r -= 1
    return ans

print(trap([0,7,1,4,6]))
print(trap([4,4,4,7,1,0]))
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
