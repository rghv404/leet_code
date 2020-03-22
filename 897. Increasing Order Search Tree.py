'''
Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \ 
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9  

Note:

    The number of nodes in the given tree will be between 1 and 100.
    Each node will have a unique integer value from 0 to 1000.
'''

# one approach is to store all the values by inOrder traversal and then recreate the tree in increasign order
import sys
sys.path.append('./')
from BinTree import BinTree, populateTreeFromList, printTree_inOrder

def increasingBST_Basic(root: BinTree) -> BinTree:
	def helper(node:BinTree):
		if node.left: helper(node.left)
		sortedVals.append(node.value)
		if node.right: helper(node.right)

	if not root: return
	
	sortedVals = []
	helper(root)
	# start building the new Tree
	newTree = BinTree(-1)
	curr = newTree
	for i, val in enumerate(sortedVals):
		curr.right = BinTree(val)
		curr = curr.right
	return newTree.right

def increasingBST(root: BinTree) -> BinTree:
	# this appraoch aims to create the tree while we are traversing and does so in an 
	# iterative fashion
	if not root: return
	stack, node = [root], root
	newTree = BinTree(-1)
	curr = newTree
	while stack:
		while node and node.left:
			node = node.left
			stack.append(node)
		node = stack.pop()
		node.left = None
		curr.right = node
		curr = curr.right
		if node and node.right:
			node = node.right
			stack.append(node)
		else: node = None
	return newTree.right

ip = [5,3,6,2,4,"null",8,1,"null","null","null",7,9]
root = populateTreeFromList(ip)
newTree = increasingBST(root)
printTree_inOrder(newTree)

