'''
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

'''
import sys
sys.path.append('../LC2/')
import BinTree as TreeNode

def distanceK_wrong(root: TreeNode, target: TreeNode, K: int) -> [int]:
	# the approach is to kepe track of depth in a top down approach
	# keep basedpth for the target node  and as and when it is not None
	# try to equate currentNOde with baseDepth asn see if its k. if yes store
	# in variable 
	
	def traverse(node: TreeNode, target: TreeNode, currDepth:int, K: int):
		nonlocal baseDepth, res
		if not node:
			return	
		print(baseDepth, currDepth, node.value)
		if node.value == target.value:
			 baseDepth = currDepth
		if baseDepth and currDepth - baseDepth == K:
			res.append(node.value)
		traverse(node.left, target, currDepth+1, K)
		traverse(node.right,target, currDepth+1, K)
		return res

	if not root or not target:
		return
	res, baseDepth = [], None
	traverse(root, target, 0, K)
	return res

'''
Clearly, I failed to undertatnd the question. We have to basically find distnce in all directions
'''
# can be done using bfs when parent are also stored for each node
def distanceK(root: TreeNode, target: TreeNode, K: int) -> [int]:
	par = {}
	def dfs(node:TreeNode, parent = None):
		if node: 
			par[node] = parent
			dfs(node.left, node)
			dfs(node.right, node)
	dfs(root)
	# now do bfs
	level = [(target, 0)]
	res, seen = [], [target]
	while level:
		subLevel = []
		for pair in level:
			node, d = pair
			if d == K:
				res.append(node.val)
			if node and node.left and node.left not in seen : 
				subLevel.append((node.left, d+1))
				seen.append(node.left)
			if node and node.right and node.right not in seen:
				subLevel.append((node.right, d+1))
				seen.append(node.right)
			if node in par and par[node] and par[node] not in seen:
				subLevel.append((par[node], d+1))
				seen.append(par[node])
		level = subLevel
	return res


ip = [3,5,1,6,2,0,8,"null","null",7,4]
root = TreeNode.populateTreeFromList(ip)
tgt = TreeNode.BinTree(5)
res = distanceK(root, tgt, 2)
print(res)
