class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        try:
            testW = min(strs, key = len)
        except:
            return ''
        res = ''
        i = 0
        for c in testW:
            if all(c == word[i] for word in strs):
                res += c
                i += 1
            else:
                return res
        return res