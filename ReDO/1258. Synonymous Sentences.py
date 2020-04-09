'''
Given a list of pairs of equivalent words synonyms and a sentence text, Return all possible synonymous sentences sorted lexicographically.
 

Example 1:

Input:
synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]],
text = "I am happy today but was sad yesterday"
Output:
["I am cheerful today but was sad yesterday",
​​​​​​​"I am cheerful today but was sorrow yesterday",
"I am happy today but was sad yesterday",
"I am happy today but was sorrow yesterday",
"I am joy today but was sad yesterday",
"I am joy today but was sorrow yesterday"]
 

Constraints:

0 <= synonyms.length <= 10
synonyms[i].length == 2
synonyms[0] != synonyms[1]
All words consist of at most 10 English letters only.
text is a single space separated sentence of at most 10 words.

'''

def generateSentences(synonyms: [[str]], text: str) -> [str]:
	
	def dfs(text:str):
		# text_as_list = text.split()
		for i, word in enumerate(text):
			print(word)
			if word in syns:
				new_texts = [text[:i] + [syn_word] + text[i+1:] for syn_word in syns[word]]
				print(new_texts)
				for newtext_as_list in new_texts:
					newtext = " ".join(newtext_as_list)
					if newtext not in resultSet:
						resultSet.add(newtext)
						dfs(newtext_as_list)


	# create a dict for synonyms
	if not synonymous:
		return [[text]]

	syns = dict()
	for pair in synonymous:
		a, b = pair
		syns.setdefault(a, []).append(b)
		syns.setdefault(b, []).append(a)

	print(syns)
	resultSet = set()
	resultSet.add(text)
	dfs(text.split())
	return list(resultSet)


synonymous = [["sad", "sorrow"], ["sad", "bad"]]
text = "Hi sad I'm bad"
res = generateSentences(synonymous, text)
print(res)