'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]

'''
import sys
sys.path.append('./')
from BinTree import BinTree, populateTreeFromList, printTree_inOrder

def zigzagLevelOrder(root: BinTree) -> [[int]]:
	# planning to do a level order traversal and then reverse the order
	# of every alternate sub array
	if not root: return 
	level, res = [root], [[root.value]]
	i = 0
	while level:
		newLevel, tempRes = [], []
		i += 1
		for node in level:
			if node.left: 
				newLevel.append(node.left)
				tempRes.append(node.left.value)
			if node.right:
				newLevel.append(node.right)
				tempRes.append(node.right.value)
		level = newLevel
		if i % 2:
			if tempRes: res.append(tempRes[::-1])
		else:
			if tempRes: res.append(tempRes)
	return res

ip = [5,3,6,2,4,"null",8,1,"null","null","null",7,9]
root = populateTreeFromList(ip)
res = zigzagLevelOrder(root)
print(res)