class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # MANACHERs ALGORITHM
        s_ = '#'.join(c for c in s)
        s_ = '$#' + s_ + '#@'
        p_len = [0] * len(s_)
        c, R = 0, 0
        for i in range(1, len(s_) - 1):
            mirr = 2*c - i
            if i < R:
                p_len[i] = min(R - i, p_len[mirr])
            while s_[i + 1 + p_len[i]] == s_[i - (1 + p_len[i])]:
                p_len[i] += 1
            
            if (i + p_len[i] > R):
                c = i
                R = i + p_len[i]
        step = max(p_len)
        index_ = p_len.index(step)
        res = s_[index_- step :index_] + s_[index_: index_ + step]
        res = res.replace('#', '')
        res = res.replace('$', '')
        res = res.replace('@', '')
        return res
                    
        
        