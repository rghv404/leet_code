'''
Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.

 

Example 1:

Input: [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.

'''

# this is an important question to make sure that dry run is extemely important and 
# that you should reach an answer in teh nb first to understand the question
import sys
sys.path.append('../../')
import BinTree as TreeNode

def distributeCoins(root: TreeNode) -> int:
	if not root:
		return 0
	def dfs(root: TreeNode) -> int:
		if not root:
			return 0,0
		lbal, lcnt = dfs(root.left)
		rbal, rcnt = dfs(root.right)
		currBal = lbal + rbal + root.value - 1
		currCnt = lcnt + rcnt + abs(currBal)
		return currBal, currCnt

	_, res = dfs(root)
	return res


ip = [1,3,0,1,0,1,1]
root = TreeNode.populateTreeFromList(ip)
print(distributeCoins(root))