'''
Implement a data structure supporting the following operations:

	Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
	Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
	GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
	GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".

Challenge: Perform all these in O(1) time complexity. 
'''

import heapq as hq
class AllOne:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.myDict = {}
		self.minmaxHeap = [] # heap from empty list
		self.removed = set()

	def inc(self, key: str) -> None:
		"""
		Inserts a new key <Key> with value 1. Or increments an existing key by 1.
		"""
		if key in self.myDict:
			self.myDict[key] += 1
			self.removed.add((self.myDict[key] - 1, key))
		else:
			self.myDict[key] = 1
		hq.heappush(self.minmaxHeap, (self.myDict[key], key))
		

	def dec(self, key: str) -> None:
		"""
		Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
		"""
		if key in self.myDict and self.myDict[key] > 1:
			self.myDict[key] -= 1
			# if reduced value has been set as self.removed in the minmax heap then make it available again i.e. remove from self.removed lull
			if (self.myDict[key], key) in self.removed:
				self.removed.remove((self.myDict[key], key))
				self.removed.add((self.myDict[key]+1, key))
		else:
			self.removed.add((self.myDict[key], key))
			del self.myDict[key]
			
		

	def getMaxKey(self) -> str:
		"""
		Returns one of the keys with maximal value.
		"""
		if not self.minmaxHeap:
			return ''
		maxItem = hq._heappop_max(self.minmaxHeap)
		while self.minmaxHeap and maxItem in self.removed:
			maxItem = hq._heappop_max(self.minmaxHeap)
		return maxItem[0]
			

	def getMinKey(self) -> str:
		"""
		Returns one of the keys with Minimal value.
		"""
		if not self.minmaxHeap:
			return ''
		minItem = hq.heappop(self.minmaxHeap)
		while self.minmaxHeap and minItem in self.removed:
			minItem = hq.heappop(self.minmaxHeap)
		return minItem[0]
		
# owow wgat a fucked up convoluted solution , could've just used two dicts if I was going to solve it in o(nlog n) anyway

# th real O(1) solution uses doubly linkedlists 

# Your AllOne object will be instantiated and called as such:
import collections
class Node:
	# node which keeps bucket of keys and itself acts as a freq
	def __init__(self):
		# a set containing keys for this node freq
		self.keySet = set()
		self.next, self.prev = None, None

	def addKey(self, key:str):
		self.keySet.add(key)

	def removeKey(self, key:str):
		self.keySet.remove(key)

	def getAnyKey(self)->str:
		item =  self.keySet.pop()
		# add it back because we don't actually want ot pop it
		self.addKey(item)
		return item

	def isEmpty(self) -> bool:
		return len(self.keySet) == 0

class DoubleLinkedList:
	def __init__(self):
		self.head = Node()
		self.tail = Node()
		self.head.next = self.tail
		self.tail.prev = self.head
		
	def insertAfter(self, x:Node):
		node, tmp = Node(), x.next
		tmp.prev, x.next = node, node
		node.prev, node.next = x, tmp
		return node

	def insertBefore(self, x:Node):
		return self.insertAfter(x.prev)

	# remove node if the bucket it represetns is empty
	def remove(self, x:Node):
		prevNode, nextNode = x.prev, x.next
		prevNode.next, nextNode.prev = nextNode, prevNode

	def getHead(self):
		return self.head.next

	def getTail(self):
		return self.tail.prev

	def getSentinelHead(self):
		return self.head

class SolutionTwo:
	def __init__(self):
		self.linkedBuckets, self.keyCounter = DoubleLinkedList(), collections.defaultdict(int)
		self.freqNodeMap = {0: self.linkedBuckets.getSentinelHead()}

	def inc(self, key:str):
		self.keyCounter[key] += 1
		currFreq, prevFreq = self.keyCounter[key], self.keyCounter[key] - 1
		# add it to freq node map if not present already
		if currFreq not in self.freqNodeMap:
			self.freqNodeMap[currFreq] = self.linkedBuckets.insertAfter(self.freqNodeMap[prevFreq])
		# add key to node set
		self.freqNodeMap[currFreq].addKey(key)
		# remove from prev Freq if more than 0
		if prevFreq > 0:
			self.freqNodeMap[prevFreq].removeKey(key)
			if self.freqNodeMap[prevFreq].isEmpty:
				self.linkedBuckets.remove(self.freqNodeMap[prevFreq])
				self.freqNodeMap.pop(prevFreq)


	def dec(self, key:str):
		# dec key if more than one otherwise remove the key, if key not in dict then return false
		if key not in self.keyCounter:
			return
		self.keyCounter[key] -= 1
		currFreq, prevFreq = self.keyCounter[key], self.keyCounter[key] + 1
		# we need to delete if currFreq was 0
		if currFreq == 0:
			self.keyCounter.pop(key)
		# check if currFreq does not exist then create it, possible if that freq ever got empty and was thus removed
		else:
			if currFreq not in self.freqNodeMap:
				self.freqNodeMap[currFreq] = self.linkedBuckets.insertBefore(self.freqNodeMap[prevFreq])
			self.freqNodeMap[currFreq].addKey(key)
		# remove key from prev node an delete it if it's empty
		self.freqNodeMap[prevFreq].removeKey(key)
		if self.freqNodeMap[prevFreq].isEmpty():
			self.linkedBuckets.remove(self.freqNodeMap[prevFreq])
			self.freqNodeMap.pop(prevFreq)

	def getMaxKey(self)->str:
		return self.linkedBuckets.getTail().getAnyKey()

	def getMinKey(self)->str:
		return self.linkedBuckets.getHead().getAnyKey()


		

obj = SolutionTwo()
key = 'a'
obj.inc(key)
obj.inc(key)
obj.inc(key)
obj.inc(key)
obj.inc(key)
key2 = 'b'
obj.inc(key2)
obj.inc(key2)
obj.inc(key2)
obj.inc(key2)

obj.dec(key)
obj.dec(key)
obj.dec(key)
obj.dec(key2)
obj.dec(key2)
obj.inc('c')
# print(obj.myDict)
# print(obj.minmaxHeap)
# print(obj.removed)
for key, val in obj.freqNodeMap.items():
	print(key, val.keySet)
param_3 = obj.getMaxKey()
param_4 = obj.getMinKey()
print(param_3, param_4)