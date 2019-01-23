# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs_orig(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        first = second = prev = dummy
        first = first.next
        second = first.next
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

    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        res = point = dummy
        point.next = head
        while point.next and point.next.next:
            save = point.next.next
            point.next.next = save.next
            save.next = point.next
            point.next = save
            point = point.next.next
        # printList(res.next)
        return res.next


def printList(head):
    node = head
    while node != None:
        print(node.val)
        node = node.next
