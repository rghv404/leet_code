''''iven a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].'''

# though about htis for half an hour almost
# can;'t think beyon stupid if else logic tbgh
# string like **(***)(**
def checkValidString(s: str) -> bool:
	stack,skip = [], 0
	for i in range(len(s)):
		if s[i] == '(':
			stack.append(s[i])
		elif s[i] == ')':
			if stack:
				stack.pop()
			elif skip > 0:
				skip -= 1 # uisng prio one asterisk as open bracket
			else: # we have extra uncalled for closed bracket rendering string bad
				return False

		else: # we  see asterisk
			skip += 1
			if stack:
				stack.pop() # using asterisk as closed bracket
				skip += 1

	if stack: # if we still have unclosed open bracket then stirng is bad
		return False
	return True


s = "()*)(*))"
s = "(*)"
print(checkValidString(s))

