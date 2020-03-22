'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its minimum depth = 2.

  There are two main methods to accomplish the min height
 DFS and BFS DFS will traverse to the lowest leaf and return minimum heioght
 while BFS will break after reaching the first leaf as we are basically doing level order traversal

 '''
import sys
sys.path.append('./LC2/')
import BinTree as TreeNode

def minDepth_DFS_recursive(root: TreeNode) -> int:
	if not root:
		return 0
	if not root.left: 
		return minDepth_DFS_recursive(root.right) + 1
	if not root.right: 
		return minDepth_DFS_recursive(root.left) + 1
	return min(minDepth_DFS_recursive(root.left), minDepth_DFS_recursive(root.right)) + 1


def minDepth_DFS_iterative(root: TreeNode) -> int:
	# it's basically sotring pair of node and dpeth in stack
	if not root:
		return 0
	stack, minDepth = [(root, 1)], float('inf')
	while stack:
		node, currDepth = stack.pop()
		if not node.left and not node.right:
			minDepth = min(minDepth, currDepth)
		if node.left: stack.append((node.left, currDepth + 1))
		if node.right: stack.append((node.right, currDepth + 1))
	return minDepth

# BFS onan average takes o(n/2) time and in worst case O(n) time and space
def minDepth_BFS_iterative(root: TreeNode) -> int:
	# levle order traversal which basically rretyurns depth at the encounter of fisrt leaf
	if not root:
		return 0
	level = [(root, 1)]
	while level:
		subLevel = []
		for pair in level:
			node, currDepth = pair
			if not node.left and not node.right:
				return currDepth
			if node.left: subLevel.append((node.left, currDepth + 1))
			if node.right: subLevel.append((node.right, currDepth + 1))
		level = subLevel


ip = [1,2,2,3,3,3,3,4,4,4,4,4,4,"null","null",5,5]
ip = [20, "null", 3, 4, 5]
ip = [3, "null", 2, "null", 1, 5]
root =  TreeNode.populateTreeFromList(ip)

print(minDepth_DFS_recursive(root))
print(minDepth_DFS_iterative(root))
print(minDepth_BFS_iterative(root))