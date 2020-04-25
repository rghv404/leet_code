'''Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?'''

# below solution si not O(1) but a naiuvee version running in o(N) trime and O(n) sapce
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
       return self.convertString(S) ==  self.convertString(T)

    def convertString(self, word:str)  -> str:
        strLst = []
        for c in word:
            if c != '#':
                strLst.append(c)
            elif strLst:
                del strLst[-1]
        print(strLst)
        return ''.join(strLst)


S, T = "acb###", "###"
print(Solution().backspaceCompare(S, T))

import itertools
def backspaceCompare(S, T) -> bool:
	# USING GENERATORS:
		def getGenerator(word:str):
			skip, i = 0, len(word) - 1

			while i >= 0:
				if word[i] == '#':
					skip += 1
				elif skip:
					skip -=1
				else:
					yield word[i]
				i-=1

		s,t = getGenerator(S), getGenerator(T)
		for c1, c2 in itertools.zip_longest(s,t):
			print(c1,c2)
			if c1!=c2:
				return False
		return True

# print(backspaceCompare("abcca#cb###", "aa#bc"))
# print(backspaceCompare("b#abcabc###", "c#aa#bc"))
print(backspaceCompare("bxj##tw","bxj###tw"))

