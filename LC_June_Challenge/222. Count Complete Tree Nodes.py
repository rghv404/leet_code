'''
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
'''

# there's an obvious oslution to this which is go htough each node and count them which obviously runs in O(n) time
# but this solution doesn't take advantage of the fact that we have here a complete tree

# we can do a binary search withing binary search of just the last level of nodes such that to determine how many 
# nodes are in the last level(oinly incomplete level). To do this we perform a binary search over the range 0 -- 2**d-1 (max numeber of leaf node for a bin completer tree). At each index we see if a node exists at that index, so for a last level for above tree i.e. 4, 5, 6, null. We check in range 0 to 3 inclusive and at each index check if node exists move right if it does else move left. 
#To check if node exists we can again do a binary search from root to node moving right and left along the way
def countNodes(self, root: TreeNode) -> int:
        def depth(node:TreeNode) -> int:
            d = 0
            while node.left:
                d+=1
                node = node.left
            return d

        def exists(idx:int, d:int, node:TreeNode) -> bool:
            l, r = 0, 2**d - 1
            for _ in range(d): # we can't use while l<=r here because we want to traverse the tree in binary time using the indexes to navigate lef tor right instead of traversing the list of indexes like in original bins search
                m = (l + r )//2
                if m >= idx:
                    node = node.left
                    r = m - 1
                else:
                    node = node.right
                    l = m + 1
            return node is not None

        if not root:
            return 0
        
        d = depth(root)
        
        if d < 1:
            return 1
        
        l, r = 0, 2**d - 1
        while l<=r:
            m = (l+r)//2
            if exists(m, d, root):
                l = m+1
            else:
                r = m-1
        
        return 2**d-1 + l
