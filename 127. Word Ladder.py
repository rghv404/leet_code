'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

    Only one letter can be changed at a time.
    Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:

    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

'''


def getTransformationSet(beginWord:str, wordSet: (str)) -> set():
	returnSet = set()
	for word in wordSet:
		if sum(1 for c1, c2 in zip(word, beginWord) if c1 != c2) == 1:
			returnSet.add(word)
	return returnSet


def ladderLength_TLE(beginWord: str, endWord: str, wordList: [str]) -> int:
	wordSet = set(wordList)
	if endWord not in wordSet:
		return 0

	minCount = float('inf')

	def traverse(beginWord: str, endWord: str, wordSet: (str), count:int) -> int:
		nonlocal minCount

		if beginWord == endWord:
			minCount = min(minCount, count)
			return

		transformedWords = getTransformationSet(beginWord, wordSet)
		print(beginWord, count, transformedWords, wordSet, minCount)
		if not transformedWords:
			return
		for word in transformedWords:
			newSet = wordSet - transformedWords
			traverse(word, endWord, newSet, count + 1)


	traverse(beginWord, endWord, wordSet, 0)

	return minCount+1 if minCount != float('inf') else 0


# above soltution do work but is not optimum to say the least and goes TLE on LC

# a simpler solution is to basically do BFS on all neighbtors and return depth once we find endWord
from collections import deque
def ladderLength_basic(beginWord: str, endWord: str, wordList: [str]) -> int:
	wordSet = set(wordList)
	if endWord not in wordSet:
		return 0
	queue, visited = deque(), set(beginWord)
	queue.append((beginWord, 1))
	while queue:
		word, count = queue.popleft()	# this takes o(n) time (when used as normal list) cause we're essentailly rebui,ding the list agian after popping first element
		# we can use collections dequeue
		for neigh in getTransformationSet(word, wordSet):
			if neigh == endWord:
				return count + 1
			elif neigh not in visited:
				queue.append((neigh, count + 1))
				visited.add(neigh)
	return 0

# the above solution works fine but for each word it take O(n) time to find it's neightbor
# we can reduce this time using an adjacency list of neigbors which can be build from regex repre of the word as key
# regex repr would be say for hot -> h*t, *ot, ho* . This will help build 1-char diff neigbor lsit with eaach intermediate
# as the key so h*t as key will have all words as values whose interme regex repre is h*t (hot, hit, hat etc)

def createAdjancyDict(wordList:[int]) -> dict():
	adjMap = dict()
	for word in wordList:
		intermediateWord = [''.join(word[:i] + '*' + word[i+1:]) for i in range(len(word))]
		# print(intermediateWord)
		for key in intermediateWord:
			adjMap.setdefault(key, []).append(word)
	return adjMap

def getNeighbors(word:str, adjMap:{})-> (str):
	interMediateKeys = [''.join(word[:i] + '*' + word[i+1:]) for i in range(len(word))]
	res = []
	for key in interMediateKeys:
		if key in adjMap:
			res.extend(adjMap[key])
	return set(res)

def ladderLength(beginWord: str, endWord: str, wordList: [str]) -> int:
	wordSet = set(wordList)
	if endWord not in wordSet:
		return 0
	queue, visited = deque(), set(beginWord)
	queue.append((beginWord, 1))
	adjMap = createAdjancyDict(wordSet)

	while queue:
		word, count = queue.popleft()	# this takes o(n) time (when used as normal list) cause we're essentailly rebui,ding the list agian after popping first element
		# we can use collections dequeue
		for neigh in getNeighbors(word, adjMap):
			if neigh == endWord:
				return count + 1
			elif neigh not in visited:
				queue.append((neigh, count + 1))
				visited.add(neigh)
	return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "hat", "pit", "dot","dog","lot","log","cog"]
# minCount = ladderLength(beginWord, endWord, wordList)
map_ = createAdjancyDict(wordList)
res = getNeighbors(beginWord, map_)
# print(minCount)
print(res)