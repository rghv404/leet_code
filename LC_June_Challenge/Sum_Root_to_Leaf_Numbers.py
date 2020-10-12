'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.


'''
import sys
sys.path.append('../')
import BinTree as TreeNode

def sumNumbers_nw(root: TreeNode) -> int:
	res = 0
	def helper(root:TreeNode):
		nonlocal res

		if not root:
			return 0

		lPow = 1 + helper(root.left)
		# lPow += 1
		res += (10**(lPow - 1))*root.value
		print('left: ', lPow, res, 'root val:,', root.value)

		rPow = helper(root.right)
		rPow += 1
		res += (10**(rPow - 1))*root.value
		print('right: ', rPow, res, 'root val:,', root.value)
		print()

		if lPow == rPow or lPow >= rPow:
			return lPow
		return rPow

	# _, op = helper(root)
	helper(root)
	return res

# the major problem with my approach is that I'm doin an inOrder traversal which causes a double sum at root.
# chagning it to pre Order traversal with an top down approach will solve this double sum probelm
def sumNumbers(root: TreeNode) -> int:
	rootToLeaf = 0
	def helper(root:TreeNode, currSum:int):
		nonlocal rootToLeaf
		if not root: return
		
		currSum = 10 * currSum + root.value
		print(currSum)
		if not root.left and not root.right:
			print(currSum)
			rootToLeaf += currSum

		helper(root.left, currSum)
		helper(root.right, currSum)

	helper(root, 0)
	return rootToLeaf


# iterative pre ROder approach
def sumNumbers(self, root: TreeNode) -> int:
    # iterative solution
    rootToLeaf = 0
    stack = [(root, 0)]
    while stack:
        root, currSum = stack.pop()
        if root is None:
            continue
        currSum = 10*currSum + root.val
        if not root.left and not root.right: # we are at leaf node, add currSum to gloabal sum
            rootToLeaf += currSum
        stack.append((root.right, currSum)) 
        stack.append((root.left, currSum))
    return rootToLeaf

ip = [4,5,2,1,"null",0]
root = TreeNode.populateTreeFromList(ip)
TreeNode.printTree_inOrder(root)
print()
op = sumNumbers(root)
print(op)