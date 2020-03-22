import sys
sys.path.append('../../LC2/')
import BinTree as TreeNode


def valid(root:TreeNode) -> bool:
	if not root:
		return 
	node = root
	minVal, maxVal = float('-inf'), float('inf')
	stack = [(root, minVal, maxVal)]
	while stack:
		node, minVal, maxVal = stack.pop()
		if node and node.right:
			stack.append((node.right, node.value, maxVal))
		if node and (node.value <= minVal or node.value >= maxVal):
			return False
		if node and node.left:
			stack.append((node.left, minVal, node.value))
	return True


def heightBalancedBinaryTree(root:TreeNode):
	def bottomUp(curr:TreeNode) -> int:
		if not curr:
			return 0
		lDepth = bottomUp(curr.left)
		if lDepth == -1: return -1

		rDepth = bottomUp(curr.right)
		if rDepth ==   -1: return -1

		if abs(lDepth-rDepth) > 1:
			return -1

		return 1 + max(lDepth, rDepth)

	if not root:
		return
	return bottomUp(root) != -1

ip = [5,1,4,"null","null",3,6]
# ip = [2,1,3]
# ip = [10,5,15,"null","null",6,20]
ip = [-28,-30,"null","null",70,"null",-19]
root = TreeNode.populateTreeFromList(ip)
print(valid(root))
print(heightBalancedBinaryTree(root))