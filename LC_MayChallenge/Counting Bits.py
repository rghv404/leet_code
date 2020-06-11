'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]

Example 2:

Input: 5
Output: [0,1,1,2,1,2]

Follow up:

    It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
    Space complexity should be O(n).
    Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

'''

def countBits(num: int) -> [int]:
	print(bin(125))
	print(bin(62), bin(61))
	if num <= 2:
		return [0,1,1]
	ans = [0,1,1]
	lastFactor, factorPwr = 2, 1
	for n in range(3,num+1):
		if 2**(factorPwr+1) == n:
			factorPwr += 1
			lastFactor = n
			ans.append(1)
			continue
		# otherwise find the diff from last perfect factor and it's number of 1s plus 1 is the answer
		minusOne = n - lastFactor
		# print(ans, n,lastFactor,minusOne)
		ans.append(ans[minusOne] + 1)
	return ans

# the above solution is what is technicaly called dynamic programming, there's a more concise way
# of solving this 
res = countBits(12)
print(res)