class Solution:
    def isValid_orig(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # complex and partial solution
        # does not cater to 
        br_d = {'(':')', '[':']', '{':'}'}
        n = len(s)
        i = 0
        if not s:
            return True
        if n % 2 != 0:
            return False
        if s[0] in br_d.values():
            return False
        while i < n:
            op_s = ''
            while  i < n and s[i] in br_d:
                op_s += s[i]
                i += 1
            l1 = [br for br in s[i: i + len(op_s)]]
            l2  =[br_d[c] for c in op_s[::-1]]
            
            if l2 != l1:
                return False
            i = i + len(op_s)
        return True
    
    def isValid(self, s):
        stack  = []
        if not s:
            return True
        if len(s) % 2 != 0:
            return False
        for br in s:
            if br in ['}', ')', ']']:
                if len(stack) == 0: return False
                top = stack.pop()
                if br == '}' and top != '{': return False
                if br == ']' and top != '[': return False
                if br ==')' and top != '(': return False
            else:
                stack.append(br)
        if len(stack) == 0:
            return True
        return False