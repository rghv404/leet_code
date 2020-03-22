import sys
sys.path.append('../../LC2/')
import BinTree as TreeNode

'''
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

Example:

Input: [1,2,3,4,5]
  
          1
         / \
        2   3
       / \     
      4   5    

Output: [[4,5,3],[2],[1]]

'''

def findLeaves_nw(root: TreeNode) -> [[int]]:
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

'''
In the above solution, I'm modifuing the list and inserting the leaf nodes at the same time
. This causes failure when a root only has left leaf node cause once the left leaf node is removed 
the root ialso becomes the leaf node adn is inserted in teh same list '''

# the solution involves getting the height of each node relative to the leaves of the tree
# no modification si needed and thus a hashmap is created with the height as key and corresponding node values
def findLeaves(root: TreeNode) -> [[int]]:
	if not root:
		return []

	def getHeight(curr:TreeNode, heightMap:dict):
		nonlocal maxHeight
		if curr is None:
			return 0
		currHeight = max(getHeight(curr.left, heightMap), getHeight(curr.right, heightMap)) + 1
		heightMap.setdefault(currHeight, []).append(curr.value)
		maxHeight = max(currHeight, maxHeight)
		return currHeight

	heightMap, maxHeight = dict(), 0
	res = []
	getHeight(root, heightMap)
	print()
	for i in range(1, maxHeight+1):
		res.append(heightMap[i])
	return res

# the above solution works only because we are measuring height from the bottom 
# and for each node we are storing it's value correpsonfing to it's depth level
# postorder traversal is used for this purpose

# another m,ehotd that I thinks hould work is bfs traversal and storing the nodes for each level
# my bad I just realized it's not gonna workd cause leaves can be in at different levels but still be leaves

ip = [1,2,3,4,5]
ip = [3, "null", 2, "null", 1]
root = TreeNode.populateTreeFromList(ip)
# TreeNode.printTree_inOrder(root)
print(findLeaves(root))