import sys
sys.path.append('./LC2/')
import BinTree as TreeNode



def leafSimilar(root1: TreeNode, root2: TreeNode) -> bool:
	# the naiuve idea is to traverse both tress separately storing the leaf nodes while doing so
	# and then comparing the leaf node list or set

	# def storeLeaves(root, leavesSet):
	# 	# this can be done in a number of ways
	# 	# dfs recurive
	# 	if root.left: storeLeaves(root.left, leavesSet)
	# 	if not root.left and not root.right: 
	# 		leavesSet.append(root.value)
	# 	if root.right: storeLeaves(root.right, leavesSet)

	def storeAndCompareLeaves(root, formerLeaves = None):
		# iterative in order traversal
		stack, node = [root], root
		currTreeLeaves = []
		while stack:
			while node and node.left:
				node = node.left
				stack.append(node)
			node = stack.pop()
			if not node.left and not node.right:
				if formerLeaves: #conpare the curr leaf with the corr leafSet
					if node.value != formerLeaves.pop(0):
						return True
				else: #we're storing first set of leaves 
					currTreeLeaves.append(node.value)
			if node and node.right:
				node = node.right
				stack.append(node)
			else:
				node = None
		return currTreeLeaves


	if not root1 or not root2:
		return True
	root1Leaves = []
	
	root1Leaves = storeAndCompareLeaves(root1)
	flag = storeAndCompareLeaves(root2, root1Leaves)

	if flag: return False
	return True
	# if root1Leaves == root2Leaves:
	# 	return True
	# return False

# create trees
# ip1 = [3,5,1,6,2,9,8,"null","null",7,4]
# ip2 = [3,5,1,6,7,4,2,"null","null","null","null","null","null",9,8]
ip1, ip2 = [1], [2]

root1 = TreeNode.populateTreeFromList(ip1)
root2 = TreeNode.populateTreeFromList(ip2)

res = leafSimilar(root1, root2)
print(res)