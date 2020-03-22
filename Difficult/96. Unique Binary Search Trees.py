'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


'''

# basically a catalan number 
# OR using the approach of chooisng a root(i) and mkaing left subtree from 1...i-1 and 
# right subtree of i...n ---> # becomes cartesian porduc tof these two parts

#cartesian prioduct apporach
def numTrees(n: int) -> int:
	tree_count = [0]*(n+1)
	tree_count[0],tree_count[1] = 1, 1

	for i in range(2, n+1):
		for j in range(1, i+1):
			tree_count[i] += tree_count[j-1] * tree_count[i-j]
	return tree_count[n]

# catalan nuber approach
# th intuition is thbat for a given n, # of unique BSTs infact follow
# a popular pattern of catalan number formula as C_n+1 = 2*C_n-1 * (2n+1)/n+2
def numTrees_catalan(n: int) -> int:
	C = 1
	for i in range(0, n):
		C *= 2*(2*i + 1)/(i +2)
	return int(C)
res = numTrees(5)
res2 = numTrees_catalan(5)
print(res, res2)