'''
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

 

Example 1:

Input: "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

'''

# the logic is simple as to keep pushing the open parenthesis in teh stack and pop whenever you see a closed one
# when tthe stack become sempty that means that we have removed teh oputer ones and
# at that index we can replace the string list with ''

def removeOuterParentheses(S: str) -> str:
	stack, list_S = [], list(S)
	start = 0
	for i in range(len(S)):
		if S[i] == '(': 
			stack.append(S[i])
		else:
			stack.pop()
		if not stack:
			# meaning we have removed the outer closing parenthesis
			list_S[start], list_S[i] = '', ''
			start = i + 1
	return ''.join(list_S)

ip = "(()())(())"
ip = "()()()"
res = removeOuterParentheses(ip)
print(res)