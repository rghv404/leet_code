'''
A starter class to create and populate Bin Tree
'''
class BinTree:
	def __init__(self, val):
		self.value = val
		self.left = None
		self.right = None

# while populating the binTree we don't check whether the val is less than root or not
# we basically populate lef tside first and then right 
def populateTreeFromList(listValues:[int]) -> BinTree:
	if not listValues or len(listValues) < 1:
		print("List given is not valid")
		return
	head = BinTree(listValues[0])
	queue = [head]
	curr, index = 0, 1
	# we begin with second elemnt in list and make it the left child
	# the subsequent element the right child if none of the is not null or None
	while index < len(listValues):

		currNode = queue[curr]
		item = listValues[index]
		if item is not None and item != 'null':
			currNode.left = BinTree(item)
			queue.append(currNode.left)
		curr += 1
		index += 1
		if index >= len(listValues): break

		item = listValues[index]
		index += 1
		if item is not None and item != 'null':
			currNode.right = BinTree(item)
			queue.append(currNode.right)
	return head


def printTree_inOrder(root:BinTree):
	if root.left: printTree_inOrder(root.left) 
	print(root.value, end = " ")
	if root.right: printTree_inOrder(root.right)

# ip = [1,2,2,3,3,3,3,4,4,4,4,4,4,"null","null",5,5]
# ip2 = [5,2,1,3,None,4,5]
# ip3 = [1,2,2,3,3,"null","null",4,4]
# root = populateTreeFromList(ip3)
# printTree_inOrder(root)