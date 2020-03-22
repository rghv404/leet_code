'''
Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
'''
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

    def printHelper(self):
    	ptr = self
    	print("Printing nodes based on next")
    	while ptr:
    		print(ptr.val, end =" ")
    		ptr = ptr.next
    	ptr = self
    	while ptr:
    		print(ptr.val, end =" ")
    		ptr = ptr.random if ptr.random else ptr.next

def copyRandomList(head: 'Node') -> 'Node':
	# return a deep copy of the head of the linked list
	# the basic trick is to make sure we do  not create two copies of the same node from 
	# either next or random. For this we use a dict with class objects as key
	# and check for those object every time we assign next and random
    if not head: return
    node_dict = {}
    def util(node:Node)-> Node:
        if node not in node_dict:
            node_dict.setdefault(node, Node(node.val, None, None))
        return node_dict[node]
    
    curr = head
    while curr:
        new = util(curr)
        if curr.next:
            new.next = util(curr.next)
        elif not curr.next:
            new.next = None
        if curr.random:
            new.random = util(curr.random)
        elif not curr.random:
            new.random = None
        curr = curr.next
    return node_dict[head]


# above method is cool but theres a strong chance that the interviewer asks for a 
# O(1) space solution. This solution is pretty interesting cause instead of using dictionary
# data structure to store unique nodes, we modify the original linked list to link the cloned list

def copyRandomList(head: 'Node') -> 'Node':
	# modify given linked list to point to cloned nodes e.g. A->B->C
	# becomes A -> A' -> B -> B' -> C -> C'
	if not head: return
	origPtr = head 
	while origPtr:
		symbiote = Node(origPtr.val, None, None)
		symbiote.next = origPtr.next
		origPtr.next = symbiote
		origPtr = symbiote.next

	# now that the list is modified with our symbiote
	# we copy the random reference to our symbiote
	origPtr = head
	while ptr:
		ptr.next.random = ptr.random.next if ptr.random else None
		ptr = ptr.next.next 

	# now that the symbiote list is complete, we need to unweave
	# i.e. remove the pointers to orginal list and free our symbiote
	ptr, ptrNew = head, head.next
	symbiote = head.next
	while ptr:
		ptr.next = ptr.next.next
		ptrNew.next = ptrNew.next.next
		ptr = ptr.next
		ptrNew = ptrNew.next

	return symbiote
