# the base code to create a linked list given an array input
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def createLinkedList(ip:[]) -> ListNode:
	if not ip:
		return None
	head = ListNode(-1) # dummy
	curr = head
	for item in ip:
		if item == "null" or item is None:
			continue
		curr.next = ListNode(item)
		curr = curr.next
	return head.next

def printLinkedList(head:ListNode):
	while head is not None:
		print(head.val, end=" ")
		head = head.next

# ip = [5,1,9]
# head = createLinkedList(ip)
# printLinkedList(head)