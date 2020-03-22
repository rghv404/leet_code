'''
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

# my naivee methjod points me not towards DP but creating perms of list 
# and then creating trees with each element as root
# once we do that we check if the created tree is a duplicate using serialization
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def generateTrees(n: int) -> [TreeNode]:
	# method to permute the list from 1...n
	
	# method to insert for each permuation
	# serialize method to further check which trees are actually unique
	def permute(arr:[int])-> [int]:
		if not arr:
			return
		if len(arr) == 1:
			return [arr]

		ret = []
		for i, item in enumerate(arr):
			remList = arr[:i] + arr[i+1:]
			for perm in permute(remList):
				ret.append([item] + perm)
		return ret

	# method to create tree for each permutation
	def createTree(root:TreeNode, value:int) -> TreeNode:
		if not root:
			return TreeNode(value)
		if root.val > value:
			# traverse left
			root.left = createTree(root.left, value)
		else:
			root.right = createTree(root.right, value)
		return root

	# serialize method to further check which trees are actually unique
	# sraialize is just a manner of storing the tree in a compact way
	# preferably in preOrder notation
	def serialize(root:TreeNode) -> [int]:
		# just gonna preOrder and return the list
		if not root:
			return
		stack, op = [root], []
		while stack:
			node = stack.pop()
			op.append(node.val)
			if node and node.right:
				stack.append(node.right)
			if node and node.left:
				stack.append(node.left)
		return op
	
	all_permuations = permute([i for i in range(1, n+1)])
	print(all_permuations)
	op, uniques = [], []
	for perm in all_permuations:
		# create BST for this pattern
		# rNode = TreeNode(perm[0])
		tree = None
		for val in perm:
			tree = createTree(tree, val)

		ser_tree = serialize(tree)

		if ser_tree not in uniques:
			uniques.append(ser_tree)
			op.append(tree)
	return op

'''
Another method is to user Dynakic programming to genrate trees for each root i (1..n)
sych that left subtree is 1...i-1 and right subtree is i+1..n
Then combine these trees, this will make sure we don't have any duplicates
'''

res = generateTrees(3)
print(res)