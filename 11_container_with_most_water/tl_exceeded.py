class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        n = len(height)
        for i in range(0, n):
            k = n - 1
            while k > i:
                area = height[i] * (k - i) if height[i] < height[k] else height[k] * (k - i)
                # print(area)
                max_area = max(area, max_area)
                k -= 1
        return max_area