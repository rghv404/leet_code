'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

    a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7

Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4

Return false.

'''
import sys
sys.path.append('./LC2/')
import BinTree as bt
# actually a height tbalacned problem can be of two types, 
# the 1st type - if any where in the tree the diff b/w deepest and highest node is maintained to be less than 2
# the 2nd type and more popular - we check balanced for each sub tree and if that sub tree is balanced we propaogate that ionfo to root node 
# the second approach is more locally placed. We explore both approached below

## 1ST APPROACH
# is simple as in we calcualte the deepest and lowest treenodes, cehck if they are fine or not.
class FirstApproach:
    def __init__(self):
        self.minLevel = float('inf')
        self.maxLevel = float('-inf')

    def depth_first_approach(self, node:bt, level:int) -> bool:
        if not node:
            self.minLevel = min(level, self.minLevel)
            self.maxLevel = max(level, self.maxLevel)
            return self.maxLevel - self.minLevel < 2

        return self.depth_first_approach(node.left, level+1) and self.depth_first_approach(node.right, level+1)

    def isBalanced(self, root:bt) -> bool:
        if not root:
            return True
        return self.depth_first_approach(root, 0)


# second class of balnced tree - formally known as height balanced tree
# for this problem as well we have two approached ONE:- Top down approach and TWO: bottom up approach

# TOP DOWN APPROACH: for each node we calculate the depth and see the difference
# curent time complxity on acverage is O(Nlogn)and worst is O(n**2 : left skewed bintree)
# cause for every node we are calculating the depth below for each node below it
class SecondApproach:
    def depth_top_down(self, node:bt) -> int:
        if not node:
            return 0
        lDepth = self.depth_top_down(node.left)
        rDepth = self.depth_top_down(node.right)
        return 1 + max(lDepth, rDepth)

    def isBalanced(self, root:bt) -> bool:
        if not root:
            return True
        lDepth = self.depth_top_down(root.left)
        rDepth = self.depth_top_down(root.right)
        return abs(lDepth - rDepth) <=1 and self.isBalanced(root.left) and self.isBalanced(root.right)

# above solution most pbbly can be modified with memoization

# BOTTOM UP APPROACH: basically return at each subTree level if they are balanced or not, propogate this info
# to upper nodes. 
class BottomUp:
    def depth_bottom_up(self, node:bt) -> int:
        if not node:
            return 0
        lDepth = self.depth_bottom_up(node.left)
        # check if lDepth is valid or not
        if lDepth == -1: return -1
        rDepth = self.depth_bottom_up(node.right)
        # check if rDepth is valid or not
        if rDepth == -1: return -1
        # we check after each step so the code returns as soon as one sub tree is invalid
        if abs(lDepth - rDepth) > 1:
            return -1
        return 1 + max(lDepth, rDepth)

    def isBalanced(self, node:bt) -> bool:
        if not root:
            return True
        return self.depth_bottom_up(root) != -1

#lets test oour current copde first
ip = [1,2,2,3,3,3,3,4,4,4,4,4,4,"null","null",5,5]
# ip = [1,2,2,3,3,"null","null",4,4]
root = bt.populateTreeFromList(ip)
# lets print mf
bt.printTree_inOrder(root)

print('First Type of Balanced: ', FirstApproach().isBalanced(root))
print('Second Type of Balanced, Top Down: ', SecondApproach().isBalanced(root))
print('Second Type of Balanced, Bottom Down: ', BottomUp().isBalanced(root))
