'''
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

 

Constraints:

    1 <= preorder.length <= 100
    1 <= preorder[i] <= 10^8
    The values of preorder are distinct.


'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertNode(currNode:TreeNode, val:int):
	if val < currNode.val:
		if currNode.left:
			insertNode(currNode.left, val)
		else:
			currNode.left = TreeNode(val, None, None)
	elif val > currNode.val:
		if currNode.right:
			insertNode(currNode.right, val)
		else:
			currNode.right = TreeNode(val, None, None)

def bstFromPreorder(preorder: [int]) -> TreeNode:
	if not preorder:
		return
	root = TreeNode(preorder[0], None, None)
	for num in preorder[1:]:
		# printFromRoot(root)
		insertNode(root,num)
	printFromRoot(root)
	return root


def printFromRoot(root:TreeNode):
	if root:
		printFromRoot(root.left)
		print(root.val, end=" ")
		printFromRoot(root.right)

# above process works in o(Nlogn) time and is not the most optimal cause for every node we are traversing
# half of the tree to find it;'s position'

def bstFromPre(preorder:[int]) -> TreeNode:
	if not preorder:
		return
	stack = []
	root = TreeNode(preorder[0])
	stack.append(root)

	for num in preorder[1:]:
		if num < stack[-1].val:
			# insert to left but don't pop and keep appending
			parent = stack[-1]
			print('LEft parent val,', parent.val)
			parent.left = TreeNode(num)
			stack.append(parent.left)
		else:
			while stack and num > stack[-1].val:
				parent = stack.pop()
				print('popped:', parent.val)
			print(parent.val)
			parent.right = TreeNode(num)
			stack.append(parent.right)
	printFromRoot(root)
	return root



rt = bstFromPre([8,5,1,7,10,12])