'''Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.'''

#Most Improtant note is taht the max diameter doesn;t necxessarily have to pass through the root node
# it is actually the max distance b/w any nodes in the tree. More cleared by the following tree
'''
[4,-7,-3,"null","null",-9,-3,9,-7,-4,"null",6,"null",-6,-6,"null","null",0,6,5,"null",9,"null","null",-1,-4,"null","null","null",-2]
In the above tree even though 4 is the root nodem, the max distance b/w two nodes (max diameter) is b/w left subtree's lead and right subtrees leaf
'''
# The solution thus becomes a little tedious in the sense that we have to keep track of left and riught subtrees depth at every sub node

import sys
sys.path.append('../')
import BinTree as TreeNode

class Solution:
    def __init__(self):
        self.ans = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.height(root)
        return self.ans

    def height(self, root) -> int:
        if not root: return 0
        left = self.height(root.left)
        right = self.height(root.right)
        self.ans = max(self.ans, left+right)
        return max(left, right) +  1

ip = [4,-7,-3,"null","null",-9,-3,9,-7,-4,"null",6,"null",-6,-6,"null","null",0,6,5,"null",9,"null","null",-1,-4,"null","null","null",-2]
root = TreeNode.populateTreeFromList(ip)
res = Solution().diameterOfBinaryTree(root)
print(res)