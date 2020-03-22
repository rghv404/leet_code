class TreeNode:
	def __init__(self, x:int):
		self.val = x
		self.left = None
		self.right = None

	def insertNode(self, value:int):
		if self.val and value:
			if value < self.val:
				if self.left:
					self.left.insertNode(value)
				else:
					self.left = TreeNode(value)

			elif value > self.val:
				if self.right:
					self.right.insertNode(value)
				else:
					self.right = TreeNode(value)
		elif value:
			self.val = value

# method to create tree
def createTree(values:[int]) -> TreeNode:
	# create root node
	if not values:
		return
	rNode = TreeNode(values[0])
	for item in values[1:]:
		rNode.insertNode(item)
	return rNode

def printTree(node: TreeNode):
	if node.left:
		printTree(node.left)
	print(node.val, end =" ")
	if node.right:
		printTree(node.right)

# define speacialized methods

#inorderTraversal
def inOrder(root:TreeNode) -> [int]:
	if not root:
		return
	node, stack, op = root, [root], []
	while stack:
		while node and node.left:
			node = node.left
			stack.append(node)
		node = stack.pop()
		op.append(node.val)
		if node and node.right:
			node = node.right
			stack.append(node)
		else:
			node = None
	return op

def levelOrder(root:TreeNode) -> [int]:
	if not root:
		return
	node, level, op = root, [root], [[root.val]]
	while level:
		newLevel, temp = [], []
		for node in level:
			if node and node.left:
				newLevel.append(node.left)
				temp.append(node.left.val)
			if node and node.right:
				newLevel.append(node.right)
				temp.append(node.right.val)
		level = newLevel
		if temp:
			op.append(temp)
	return op

# vertical Order
def verticalOrder(root:TreeNode) -> [int]:
	# basically levleoirder but gotta keep track of 
	level, vertical_dict = [(root,0)], dict()
	while level:
		newLevel, temp = [], []
		for node, i in level:
			vertical_dict.setdefault(i, []).append(node.val)
			if node and node.left:
				newLevel.append((node.left, i-1))
			if node and node.right:
				newLevel.append((node.right, i+1))
		level = newLevel
	return vertical_dict

# jsut chekcing for fukcs sake thepreorder traversal
def preOrder(root:TreeNode) -> [int]:
	if not root:return
	stack, op = [root], []
	while stack:
		node = stack.pop()
		op.append(node.val)
		if node and node.right:
			stack.append(node.right)
		if node and node.left:
			stack.append(node.left)
	return op

# left view is level order first element of each level


# rightview is last elelment of each lelvel


# bottomView


#topView


#isValid ## two appraoches 1. compare 
def isValid(root:TreeNode) -> bool:
	# iterative approach preOrder
	if not root:
		return True
	stack = [(root, float("-inf"), float("inf"))]
	while stack:
		node, lower, upper = stack.pop()
		if not node:
			continue
		if node.val <= lower or node.val >= upper:
			return False
		print(node.right.val if node.right else None, node.val, upper)
		print(node.left.val if node.left else None, lower, node.val)
		stack.append((node.right, node.val, upper))
		stack.append((node.left, lower, node.val))
	return True

#mirrorTree
def mirrorTree(head:TreeNode) -> bool:
	if not head: return True
	stack = [(head.left, head.right)]	
	while stack:
		l, r = stack.pop()
		if not l and not r:
			continue
		if (not l and r) or (not r and l) or l.val!=r.val: return False
		stack.append((l.right, r.left))
		stack.append((l.left, r.right))
	return True

#same tree


# start using the class
sampleTree = [50,20,60,None,25,55,62,12,30]
node = createTree(sampleTree)
printTree(node)
res = inOrder(node)
res2 = levelOrder(node)
res3 = verticalOrder(node)
print(res)
print(res2)
print('Vertical Order', res3)
print('PreOrder: ', preOrder(node))
print("Is valid BST: ", isValid(node))
print('Is mirror subtree: ', mirrorTree(node))