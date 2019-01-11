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
            left = height[l]
            right = height[r]
            if left < right:
                area = left * (r - l) 
                while height[l] <= left:
                    l += 1
            else:
                area = right * (r - l) 
                while height[r] <= right and r:
                    r -= 1
            max_area = max(area, max_area)
        return max_area
        
        