'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

'''
import sys
sys.path.append('../')
import BinTree as TreeNode

# seems like basic logic of traversing in order until reaching kth node
def kthSmallest_wrong(root: TreeNode, k: int) -> int:
	def helper(root:TreeNode, d: int):
		if not root:
			return
		if d == k:
			return root.value

		helper(root.left, d+1)
		helper(root.right, d+1)

	return helper(root, 0)

# above solution defies all norms of recursion man, why did you expect for the recursion stack to stop just at k
# the node traversal will keep happening and ultimately NOne will be returned. It's better to build a list usign recusion traversal above then return kth smalees elkemtn

# other method is to do sort of inordedr traversal iteratively 
def kthSmallest(root: TreeNode, k: int) -> int:
	stack, node = [], root
	while True:
		while node:
			stack.append(node)
			node = node.left
		
		node = stack.pop()
		k -= 1
		if not k:
			return node.value
		node = node.right# if node else None


# ip = [1,2,2,3,3,3,3,4,4,4,4,4,4,"null","null",5,5]
ip = [1,2,2,3,3,"null","null",4,4]
root = TreeNode.populateTreeFromList(ip)
# TreeNode.printTree_inOrder(root)
val = kthSmallest(root,2)
print(val)