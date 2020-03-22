'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

'''
import sys
sys.path.append('../../LC2/')
from BinTree import BinTree as TreeNode, printTree_inOrder
from LinkedList import ListNode, createLinkedList, printLinkedList
# my naiveee imple,entaion si to convert th elinkedlist to a list and then 
# use dfs recursively to keep dividign that list into half and making the middle value as t eh root of the usbtree

def sortedListToBST_extraStep(head: ListNode) -> TreeNode:
    
    def dfs(ip: [TreeNode]) -> TreeNode:
        # if len(ip) <= 3:
        # # we have the base subTree
        #     middleNode = len(ip)//2
        #     root = ip[middleNode]
        #     root.left = ip[middleNode-1]  if middleNode-1 >= 0 else None
        #     root.right = ip[middleNode+1] if middleNode+1 < len(ip) else None
        #     return root

        # the above condition is not neede cause i'm literally handling thje case belwo using if condition
        # it only makes it slightly faster cause otherwise it tries to partiton it as well
        if len(ip) == 1:
            return ip[0]

        middleNode = len(ip)//2
        root = ip[middleNode]
        if ip[:middleNode]:
            root.left = dfs(ip[:middleNode])
        if ip[middleNode+1:]:
            root.right = dfs(ip[middleNode+1:])
        return root

    if not head:
        return
    TreeNodeList = []
    curr = head
    # we also in the travelsal majke the listnode obj to treenode w/o any left or right
    while curr:
        TreeNodeList.append(TreeNode(curr.val))
        curr = curr.next

    return dfs(TreeNodeList)

# below method uses slow and fast pointer to divide the left and right subtrees
def sortedListToBST(head: ListNode) -> TreeNode:
    def toTree(head:ListNode, tail:TreeNode):
        if head == tail:
            return None
        slow, fast = head, head
        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next
        root = TreeNode(slow.val)
        root.left = toTree(head, slow)
        root.right = toTree(slow.next, tail)
        return root

    if not head: return
    return toTree(head, None)

initialList = [2,3,4,5,6,7]
initialList = [-10,-3,0,5,9]
initialList = [0,2,3]
head = createLinkedList(initialList)
# printLinkedList(head)

root = sortedListToBST(head)
print(root.value)
printTree_inOrder(root)