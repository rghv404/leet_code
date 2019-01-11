class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # s_ = s[::-1]
        if len(s) == 1:
            return s
        s_ = '@'+ s +'@'
        n = len(s_)
        res = ''
        for i in range(n-2):
            j = i + 1
            while j < n:
                if s_[i] in s_[i+1:j+1] and s_[i:j+1] == s_[j:i-1:-1]:
                    if len(res) < len(s_[i:j+1]): res = s_[i:j+1] 
                j+=1
        if len(res) == 0 and len(s) != 0:
            return s[0]
        return res
                
        
        