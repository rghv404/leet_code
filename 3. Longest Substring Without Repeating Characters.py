'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


'''

# There are basically two approaches, 1 - keep a set of unique words and when a repeaitrng letter is encountere we empty 
# the set until all letter upto the one encoutered is removed. Time complexity o(2*n) = O(n) and space O(m)


def lengthOfLongestSubstring(s: str) -> int:
	i, j, count, res = 0, 0, 0, 0
	n, uniqueSet = len(s), set()
	while i < n and j < n:
		if s[i] not in uniqueSet:
			count = i - j + 1
			res = max(res, count)
			uniqueSet.update(s[i])
			i += 1
		else:
			uniqueSet.remove(s[j])
			j += 1
	return res, uniqueSet

# if we also need to return longest substring than instead of set use orderdSet or a list lets keep list instead for simplicity
def lengthOfLongestSubstring_and_substring(s: str) -> int:
	i = j = count = res = 0
	n, uniqueList  = len(s), []
	longestSubString = []
	while i < n and j < n:
		if s[i] not in uniqueList:
			count = i - j + 1
			uniqueList.append(s[i])
			if res <= count:
				print(' CAhnging stuff', res, count)
				res = count
				longestSubString = uniqueList[:]
			i += 1
		else:
			uniqueList.remove(s[j])
			j += 1
			
	return res, uniqueList, "".join(longestSubString)

# Second approach - the reason for O(2n) is that we when removing we are actually visiting letter i owrst acse twice
# to handle this in O(n) time, we keep a dictionary of indexes and simple skip that much
def lengthOfLongestSubstring_seconbdApproach(s: str) -> int:
	indexBucket = dict()
	start = 0 	# start is used to check if the current repeating letter index and it's previous index contains any repeating chars
	res, count = 0, 0
	for i, letter in enumerate(s):
		if letter in indexBucket and indexBucket[letter] >= start:
			res = max(count, res)
			count = i - indexBucket[letter]
			start = indexBucket[letter] + 1 # update to current no repeat index
		else:
			count += 1
		# print(i, letter, count)
		indexBucket[letter] = i
	return max(res, count)

# another optimized approach to not have xtra vars and stuff
def lengthOfLongestSubstring_seconbdApproach_optimized(s:str):
	res = start = 0
	indexBucket = dict()
	for i, letter in enumerate(s):
		if letter in indexBucket and indexBucket[letter] >= start:
			start = indexBucket[letter] + 1
		else:
			res = max(res, i - start + 1)
		indexBucket[letter] = i
	return res

# let's test the first approach
ip = "abcdabcdbbdvdef"
# ip = "pwwkew"
print(lengthOfLongestSubstring(ip))
print(lengthOfLongestSubstring_and_substring(ip))
print(lengthOfLongestSubstring_seconbdApproach(ip))
print(lengthOfLongestSubstring_seconbdApproach_optimized(ip))