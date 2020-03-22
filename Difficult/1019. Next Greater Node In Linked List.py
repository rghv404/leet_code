'''We are given a linked list with head as the first node.  Let's number the nodes in the list: node_1, node_2, node_3, ... etc.

Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val such that j > i, node_j.val > node_i.val, and j is the smallest possible choice.  If such a j does not exist, the next larger value is 0.

Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).

Note that in the example inputs (not outputs) below, arrays such as [2,1,5] represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.

 

Example 1:

Input: [2,1,5]
Output: [5,5,0]
'''
import sys
sys.path.append('../LC2/')
import LinkedList as ListNode
def nextLargerNodes_naivee(head: ListNode) -> [int]:
	if not head:
		return []
	curr, res = head, []
	while curr is not None:
		currVal = curr.val
		nextNode = curr.next
		while nextNode is not None and nextNode.val <= currVal:
			nextNode = nextNode.next
		largerVal = nextNode.val if nextNode is not None else 0
		res.append(largerVal)
		curr = curr.next
	return res

# the above solution works in O(n**2) in worst case scenario and gives TLE 
# THe below solution takes use of a stack to basically store values in incraesing order
# and popping values from the stack as soon as a value bigger is found in teh linkedlist
def nextLargerNodes(head: ListNode) -> [int]:
	stack, res = [], []
	i = -1
	while head:
		i += 1
		res.append(0)
		while stack and stack[-1][1] < head.val:
			# this means we have stumbled upon next lager value
			idx, _ = stack.pop()
			res[idx] = head.val
		stack.append((i, head.val))
		head = head.next
	return res


ip = [1,7,5,1,9,2,5,1]
head = ListNode.createLinkedList(ip)
ListNode.printLinkedList(head)
res = nextLargerNodes(head)
print(res)