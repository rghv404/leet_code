# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        first = second = prev = dummy
        first = first.next
        if first is not None:
            second = first.next
        else: return head 
        if second == None:
            return head
        while second != None:
            prev.next = first.next
            first.next = second.next
            second.next = first
            
            prev = first
            first = first.next
            if first is None:
                break
            second = first.next
        return dummy.next
        # printList(dummy.next)
            
def printList(head):
    node = head
    while node != None:
        print(node.val)
        node = node.next
    