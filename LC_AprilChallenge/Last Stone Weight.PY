'''
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
 

Note:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
'''

# naivee method - sort the array in dec order -- replace first two elems with their diff - repeat
def lastStoneWeight_naivee(stones:[int]) -> int:
	while len(stones) > 1:
		stones.sort(reverse=True)
		print('Before op: ', stones)
		elem = stones[0] - stones[1]
		del stones[:2]
		if elem != 0:
			stones.append(elem)
		print('After op: ', stones)
		
	return stones[0] if stones else 0


# above solution works in O(n**2 logn)
def getTopTwoElems(stones)->(int,int):
	lastElem, secondLastElem = (float('-inf'),0), (float('-inf'), 0)
	for i, num in enumerate(stones):
		if num >= lastElem[0]:
			secondLastElem = lastElem
			lastElem = (num, i)
		elif num >= secondLastElem[0]:
			secondLastElem = (num, i)

	return (lastElem, secondLastElem)

def lastStoneWeight_n2(stones:[int]) -> int:
	while len(stones) > 1:
		(last, lastIndex), (scndLast, scndLastInd) = getTopTwoElems(stones)
		print('Before op: ', stones, (last, lastIndex), (scndLast,scndLastInd))
		elem = last - scndLast
		del stones[lastIndex]
		if lastIndex < scndLastInd:
			del stones[scndLastInd-1]
		else:
			del stones[scndLastInd]
		if elem != 0:
			stones.append(elem)
		print('After op: ', stones)
		
	return stones[0] if stones else 0


# above solution works in O(n**2) time. The same solution but in better code is below

def lastStoneWeight(stones:[int]) -> int:
	while len(stones) > 1:
		maxElem = max(stones)
		stones.remove(maxElem)
		scndMaxElem = max(stones)
		stones.remove(scndMaxElem)
		elem = maxElem - scndMaxElem
		if elem != 0:
			stones.append(elem)

	return stones[0] if stones else 0	


# another methdo to solve in nlogn is to use maxHeap


res = lastStoneWeight([2,2,5,7,9,1])
# res = lastStoneWeight([2,2,5,56])
print(res)



