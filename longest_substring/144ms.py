class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub_count = 0
        n = len(s)
        a = set()
        i = 0; j = 0
        if len(s) == 1:
            return len(s)
        while i < n and j < n:
            if s[j] not in a:
                a.add(s[j])
                j+=1
                sub_count = max(sub_count, j - i)
            else:
                a.remove(s[i])
                i+=1
        return sub_count
        