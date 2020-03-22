'''
 Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2

Given tree t:

   4 
  / \
 1   2

'''

def isEqual(s:TreeNode, t:TreeNode) -> bool:
	
	if not s and not t:
		return True
	if (not s and t) and (not t and s):
		return False
	return isEqual(s.left, t.left) and isEqual(s.right, t.right)


def isSubtree(s: TreeNode, t: TreeNode) -> bool:
	# preOrder traversal for s tree
	if not s and not t:
		return True
	
	if (not s and t) or (not t and s):
		return False

	stack = [node]
	
	while stack:
		node = stack.pop()
		if node.val == t.val:
			flag = flag or isEqual(node.left, t.left) and isEqual(node.right, t.right) 
		if node and node.left: stack.append(node.right)
		if node and node.right: stack.append(node.left)

	return flag
