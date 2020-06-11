'''
nvert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:

    Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
'''

# here's my interative solution, basically an inroder iterative traversal with a new tree node 
# mirroring the orignal treenode's children

def invertTree_iterative(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        node, nwNode = root, TreeNode(root.val)
        stack = [(node, nwNode)]
        ans = nwNode
        
        while stack:
            while node and node.left:
                print(node.val)
                node = node.left
                nwNode.right = TreeNode(node.val)
                nwNode = nwNode.right
                stack.append((node, nwNode))
                
            node, nwNode = stack.pop()
            
            if node.right:
                node = node.right
                nwNode.left = TreeNode(node.val)
                nwNode = nwNode.left
                stack.append((node, nwNode))
            else:
                node = None
        return ans


# same ideal implement cleanly using recursion, it is highly likely i'll be implementing the iterative solution if asked in teh itnervew
# but goddamit i shoudl be familair and cofident already woth the recusrive solution

def invertTree_recursive(self, root: TreeNode) -> TreeNode:
	if not root:
		return
	leftNode = self.invertTree_recursive(root.left)
	rightNode = self.invertTree_recursive(root.right)

	root.rigth = leftNode
	root.left = rightNode

	return root

