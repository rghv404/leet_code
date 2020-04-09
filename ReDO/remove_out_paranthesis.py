# trying to tack general case when it's possible that the string is not in parathesis correct format
def remo_only_outer_paran(word:str) -> str:
	stack, start = [], ''
	res = list(word)
	flag_bracket_encounter = False
	for i in range(len(word)):
		if word[i] == '(':
			stack.append('(')
			if start == '':
				start = i
			flag_bracket_encounter = True
		elif word[i] == ')':
			stack.pop(-1)

		# when the curr group of paranthesis is over
		if not stack and flag_bracket_encounter:
			res[start], res[i]  = '', ''
			start = ''
			flag_bracket_encounter = False

	return ''.join(res)


input = "124+(567)+((345)) + (((hello)))"
res = remo_only_outer_paran(input)
print(res)

