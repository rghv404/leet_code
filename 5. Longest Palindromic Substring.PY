'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"

'''
# BRUTE FORCE METHOD
def longestPalindrome_naivee(s: str) -> str:
	mat = [[0 for _ in range(len(s))] for _ in range(len(s))]
	res = ""
	for i in range(len(mat)):
		for j in range(i, len(mat)):
			subS = s[i:j+1]
			if subS == subS[::-1]: 
				res = max((res, subS), key=len)
				mat[i][j] = len(subS)
	print(mat,res)

# the baove solution runs in O(n**3) time O(n**2) for the iterations and O(n) for stirng mathcing for each iteration


# below is the DP equivalent that runs in o(n**2) and uses O(n**2) space for the 2-d array
def longestPalindrome_DP(s: str) -> str:
	mat = [[0 for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]
	subStr = ""
	palindromeIndexes = (0,0)
	for i in range(1, len(mat)): 
		mat[i][i] = 1
		if i != len(s):
			if s[i-1] == s[i]:
				mat[i][i+1] = 1 
				palindromeIndexes = max((palindromeIndexes, (i-1, i)), key = lambda x:x[1]-x[0])
	# case when j - i > 2
	for j in range(1, len(mat)):
		for i in range(1, j+1):
			# if i == 4: print(mat[i+1][j-1], s[i-1], s[j-1])
			if j - i > 2:
				if i != len(s) and mat[i+1][j-1]==1 and s[i-1] == s[j-1]:
					mat[i][j] = 1
					palindromeIndexes = max((palindromeIndexes, (i-1, j-1)), key = lambda x:x[1]-x[0])
				elif i == len(s) and s[i-1]==s[j-1]:
					mat[i][j] = 1
					palindromeIndexes = max((palindromeIndexes, (i-1, j-1)), key = lambda x:x[1]-x[0])

	for i, row in enumerate(mat):
		print(s[i-1], row)
	i, j = palindromeIndexes
	return s[i:j+1]

# another method is expand aorun d the center
def longestPalindrome(s: str) -> str:
	def expand(s, l, r):
		while (l >= 0 and r < len(s) and s[l] == s[r]):
			l-=1; r+= 1;
		return (l+1, r-1)  
	
	indexes = (0, 0)

	for i in range(len(s)):
		# we expanmd in two ways to take care of even/odd length of palindrome strings
		len1 = expand(s, i, i)	# of length
		len2 = expand(s, i, i+1)
		indexes = max((indexes, len1, len2), key=lambda x:x[1] - x[0])
	return (s[indexes[0]: indexes[1] + 1])

s = "elemnonmtet"
# s = "cbbd"
# s = "abaabc"
# s = "bb"
print(longestPalindrome(s))