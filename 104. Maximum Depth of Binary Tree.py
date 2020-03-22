'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its depth = 3.

'''
import sys
sys.path.append('./')
from BinTree import BinTree, populateTreeFromList

def maxDepth(root: BinTree) -> int:
	def helper(node:BinTree, h:int)-> int:
		if not node:
			return h
		return max(helper(node.left, h+1), helper(node.right, h+1))

	if not root: return 0
	return helper(root, 0)

# iterative solution in preOrder manner
def maxDepth_Iterative(root: BinTree) -> int:
	if not root: return 0
	maxDepth = 0
	stack, res = [(root, 0)], []
	while stack:
		node, currHeight = stack.pop()
		if maxDepth < currHeight:
			maxDepth = currHeight
		res.append(node.value)
		if node.right: stack.append((node.right, currHeight+1))
		if node.left: stack.append((node.left, currHeight+1))
	print(res)
	return maxDepth+1


# ip = [1,2,2,3,3,3,3,4,4,4,4,4,4,"null","null",5,5]
ip = [3,9,20,"null","null",15,7]
root = populateTreeFromList(ip)
res = maxDepth_Iterative(root)
print(res)
