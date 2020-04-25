'''Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.'''


# my naivee metthod to handle this opwuld be to create a set of literals for each word and then equate all the sets
def groupAnagrams_setMethod(strs: [str]) -> [[str]]:
	seen, res = set(), []
	for i in range(len(strs)):
		if i in seen:
			continue
		temp = []
		for j in range(i+1, len(strs)):
			if j not in seen and set(strs[i]) == set(strs[j]):
				temp.append(strs[j])
				seen.add(j)
		# add pivot word to seeen and to result if result exists
		seen.add(i)
		temp.append(strs[i])
		res.append(temp)

	return res

# the above solution is obviously flwaed because set comparison fails when duplciarte letter are present in the word
# for e.g. "bob" and "boo" will be equated as equals

# the other method that comes to mind is create perms for each word and then see if those words are present in the list
def groupAnagrams_AllPerms(strs:[str]) -> [[str]]:
	if not strs:
		return

	def findPerms(word:[str]):#, res: [str]):
		if not word:
			return

		if len(word) == 1:
			if word in wordSet:
				currAnagrams.add(word)
			return [word]
		
		ret = set()

		for i, letter in enumerate(word):
			remWord = word[:i] + word[i+1:]
			# print(remWord)
			for perm in findPerms(remWord):
				# check if new string in 
				newWord = "".join([letter] + [perm])
				print(newWord)
				if newWord in wordSet:
					currAnagrams.add(newWord)
				ret.add(newWord)
		return ret
	# handle empty strings
	res = []
	empty = [word for word in strs if word == ""]
	if empty:res.append(empty)

	# now only proper word remains
	seen, wordSet = set(), set(strs)
	for word in strs:
		currAnagrams = set()
		if word in seen:
			continue
		findPerms(word)
		if currAnagrams:
			res.append(list(currAnagrams))
			seen.update(currAnagrams)
	return res


# an even simpler methos is to create tuple of count of alphabets for each word and create a dict
# for this tuple with all words as value to the tuple key 
# for e.g. eat and ate both have 1 a and 1 e and 1 t such that the alphabet tuple will be (0,0,..)
# with all the way to 26th letter and have 1, 1, 1 at each a, e and t letters
# this tuple in dict will have both words, essentailly this is how the question wants us to do the problem
# all other ways are too complicated

def groupAnagrams(strs:[str]) -> [[str]]:
	res = dict()
	for word in strs:
		alphabetList = [0]*26 # a list of 26 zeroes each index corressponds to an alphabet
		for c in word:
			alphabetList[ord(c) - ord('a')] += 1
		res.setdefault(tuple(alphabetList), []).append(word)
	return list(res.values())

ip = ["eat", "tea", "tan", "ate", "nat", "bat"]
ip = ["", "", ""]
# ip = ["a", "a"]
ip = ["hos","boo","nay","deb","wow","bop","bob","brr","hey","rye","eve","elf","pup","bum","iva",
"lyx","yap","ugh","hem","rod","aha","nam","gap","yea","doc","pen","job","dis","max","oho","jed","lye",
"ram","pup","qua","ugh","mir","nap","deb","hog","let","gym","bye","lon","aft","eel","sol","jab"]
res = groupAnagrams(ip)
# print(sorted(ip))
print(res)
# res= createPerms("eat")
# print(res)