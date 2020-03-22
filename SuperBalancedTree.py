'''
Write a function to see if a binary tree ↴ is "superbalanced" (a new tree property we just made up).

A tree is "superbalanced" if the difference between the depths of any two leaf nodes ↴ is no greater than one.
'''
import sys
sys.path.append('../LC2/')
import BinTree as TreeNode
def superBalanced_recursive(root: TreeNode) -> bool:
	maxHeight = float('-inf')
	minHeight = float('inf')
	def check(node: TreeNode, depth:int) -> bool:
		
		nonlocal maxHeight, minHeight
		if not node:
			return depth
		lHeight = check(node.left, depth + 1)
		rHeight = check(node.right, depth + 1)
		print(node.value, lHeight, rHeight)
		# if abs(lHeight - rHeight) > 1:
		# 	return False
		minHeight = min(minHeight, lHeight, rHeight)
		maxHeight = max(maxHeight, lHeight, rHeight)
		print(node.value, 'maxH', maxHeight, 'minH', minHeight)
		if maxHeight - minHeight > 1:
			return False
		return max(lHeight, rHeight)

	return True if check(root, 0) else check(root, 0)

def superBalanced(root: TreeNode) -> bool:
	if not root:
		return True
	level = [(root, 0)]
	minH, maxH = float('inf'), float('-inf')
	while level:
		subLevel = []
		for pair in level:
			node, depth = pair
			if not node.left and not node.right:
				minH = min(minH, depth)
				maxH = max(maxH, depth)
				print(node.value, minH, maxH)
			if node and node.left: subLevel.append((node.left, depth+1))
			if node and node.right: subLevel.append((node.right, depth+1))
		level = subLevel

	return maxH - minH < 2

ip = [1,2,2,3,3,3,3,4,4,4,4,4,4,"null","null",5,5]
ip = [1,2,2,3,3,"null","null",4,4]
# ip = [3,5,1,6,2,0,8,"null","null",7,4]
# ip = [1,2,3]
root = TreeNode.populateTreeFromList(ip)

res = superBalanced_recursive(root)
print(res)