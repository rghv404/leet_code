import sys
sys.path.append('./LC2/')
import BinTree as TreeNode



def findLeaves(root: TreeNode) -> [[int]]:
	def traverseAndUpdateTree(root, prev, dir, currLeaves):
		if root and root.left: traverseAndUpdateTree(root.left, root, "left", currLeaves)
		if not root.left and not root.right:
			if dir == "left":
				currLeaves.append(root.value)
				prev.left = None
			elif dir == "right":
				currLeaves.append(root.value)
				prev.right = None
			else: # only root remains
				root = None
		if root and root.right: traverseAndUpdateTree(root.right, root, "right", currLeaves)


	if not root:
		return [[]]
	res = []
	while root.left or root.right:
		currLeaves = []
		traverseAndUpdateTree(root, None, "", currLeaves)
		print(currLeaves)
		res.append(currLeaves)
	res.append([root.value])
	root = None
	return res

ip = [1,2,3,4,5]
root = TreeNode.populateTreeFromList(ip)
print(findLeaves(root))
