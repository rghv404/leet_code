'''
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
'''
import collections
def minDistance(word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        print(dp)
        for i in range(n+1):
            for j in range(m+1):
            	if i == 0:
            		dp[i][j] = j
            	elif j == 0:
            		dp[i][j] = i
            	# when word at i-1 and j-1 are equal then i, j are equal to the value in i-1, j-1 cell
            	elif word1[i-1] == word2[j-1]:
            		dp[i][j] = dp[i-1][j-1]
            	else:
            		dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        print(dp)
        return dp[n][m]

# can we use a dict instead of a 2d matri, it'd still take O(nm) time and space but less code
def minDistance_withDict(word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = collections.defaultdict(int) #[[0 for _ in range(m+1)] for _ in range(n+1)]
        
        for i in range(n+1):
            for j in range(m+1):
            	if i == 0:
            		dp[i, j] = j
            	elif j == 0:
            		dp[i, j] = i
            	# when word at i-1 and j-1 are equal then i, j are equal to the value in i-1, j-1 cell
            	elif word1[i-1] == word2[j-1]:
            		dp[i, j] = dp[i-1, j-1]
            	else:
            		dp[i, j] = 1 + min(dp[i-1, j], dp[i, j-1], dp[i-1, j-1])
        return dp[n, m]


w1 = "TOM"
w2 = "JIM"
res = minDistance(w1, w2)
res2 = minDistance_withDict(w1, w2)
print(res)