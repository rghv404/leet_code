class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub_count = 0
        a = ''
        if len(s) == 1:
            return len(s)
        for i in range(len(s) - 1):
            a = s[i]
            for j in range(i+1, len(s)):
                if s[j] in a:
                    break;
                a += s[j]
            if len(a) > sub_count:
                sub_count = len(a)
        return sub_count
        
            