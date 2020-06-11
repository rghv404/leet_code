'''
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.
 

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

'''

# the idea here is to place the tallest nodes first ordered by their k value
# and then contnuosly place next tallest based on their k values in b/w the tallest nodes
# so basically sort the nodes depending from tallest to shortes and then 

def reconstructQueue(people: [[int]]) -> [[int]]:
	people.sort(key = lambda x: (-x[0], x[1]))
	op = []
	for val, pos in people:
		op.insert(pos, [val, pos])
	return op


ip = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
res = reconstructQueue(ip)
print(res)