'''
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.

Write a function that takes an integer n and return all possible combinations of its factors.

Note:

    You may assume that n is always positive.
    Factors should be greater than 1 and less than n.

Example 1:

Input: 1
Output: []

Example 2:

Input: 37
Output:[]

Example 3:

Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]

Example 4:

Input: 32
Output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]


'''
res = []
def helper(num:int) -> [[int]]:
	if num == 1:
		return 

	for i in range(2, int(num**0.5) + 1):
		temp =[]
		if num % i == 0:
			temp.append([i, num//i])
		res.append(temp)
		helper(num//i)
	return res

def getFactors(n: int) -> [[int]]:
	return helper(n)

res = getFactors(32)
print(res)