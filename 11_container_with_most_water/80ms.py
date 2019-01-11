class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        n = len(height)
        l = 0
        r = n - 1
        while l < r:
                area = min(height[l], height[r]) * (r - l) 
                max_area = max(area, max_area)
                if height[l] < height[r]:
                    l += 1
                else:
                    r -= 1
        return max_area
        
        