'''
Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.

A node is deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is that node, plus the set of all descendants of that node.

Return the node with the largest depth such that it contains all the deepest nodes in its subtree.

 

Example 1:

Input: [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation:

We return the node with value 2, colored in yellow in the diagram.
The nodes colored in blue are the deepest nodes of the tree.
The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
Both the input and output have TreeNode type.

'''
import sys
sys.path.append('../../LC2/')
import BinTree as TreeNode
def subtreeWithAllDeepest_naivee_nw(root: TreeNode) -> TreeNode:
	hashmap = {}#{(2,5,1,2):(3), (6,2,0,8):(5,1), (7,4,1,0):(2,0)}
	level = [root]
	while len(level) > 0:
		subLevel, subLevelParents = [], []
		for node in level:
			if node.left: 
				subLevel.append(node.left)
				subLevelParents.append(node)
			if node.right:
				subLevel.append(node.right)
		level = subLevel
		if len(subLevel) > 0:
			lastLevel = subLevel
			hashmap[tuple(subLevel)] = subLevelParents
	key = tuple(lastLevel)
	while len(hashmap[key]) != 1:
		key = [newKey for newKey in hashmap.keys() if set(hashmap[key]).issubset((newKey))][0]
		print(key)
	return hashmap[key]

def subtreeWithAllDeepest(root: TreeNode) -> TreeNode:
	# basica idea is to find all deepst lelvle nodes using BFS(level order)
	# then apply least comon ancestor logic to find lca for the above nodes
	if not root:
		return None
	level, lastLevel =  [root], [root]
	while level:
		subLevel = []
		for node in level:
			if node.left: subLevel.append(node.left)
			if node.right: subLevel.append(node.right)
		level = subLevel
		if subLevel:
			lastLevel = subLevel
	res = lastLevel[0]
	for i in range(1, len(lastLevel)):
		res = lca(root, lastLevel[i], res)
	return res

def lca(node:TreeNode, l1: TreeNode, l2: TreeNode) -> TreeNode:
	# this is the base code to find the least common ancestor of a pair of nodes
	# crux of it is to do postOrder
	if not node or node==l1 or node==l2:
		return node
	left = lca(node.left, l1, l2)
	right = lca(node.right, l1, l2)

	if left is not None and right is not None:
		return node
	return left if left is not None else right


def onePass(root: TreeNode) -> TreeNode:
	def dfs(node: TreeNode) -> TreeNode:
		if not node:
			return (0, None)
		lHeight, lNode = dfs(node.left)
		rHeight, rNode = dfs(node.right)
		if lHeight == rHeight:
			return (lHeight+1, node)
		elif lHeight > rHeight:
			return (lHeight+1, lNode)
		else: return (rHeight+1, rNode)

	if not root:
		return None
	return dfs(root)[1]

ip = [3,5,1,6,2,0,8,"null","null",7,4,10]
root = TreeNode.populateTreeFromList(ip)
res = subtreeWithAllDeepest(root)
res = onePass(root)
print(res.value)
# lca_ = lca(root, root.left.left, root.right.left)
# print(lca_.value)