'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

'''
# naive solution convert list to num, ncrement one and then covnert back to list works in o(N) time
def plusOne_naivee(digits: [int]) -> [int]:
        num, n = 0, len(digits)
        for i in range(n-1, -1, -1):
            num += digits[n-i-1]*10**i
        newNum = num+1
        res = []
        # again O(n)
        while newNum:
            digit = newNum % 10
            res.append(digit)
            newNum //= 10
        return res[::-1]

# an optimization could be increment the last digit and keep ncrementing prev digit if they become 10 else return the orign list
# this owkrs in woirks case O(n) tiem but average ase is iproved

def plusOne(digits: [int]) -> [int]:
	digits[-1] += 1
	i = len(digits) - 1
	while i >= 0 and digits[i] == 10:
		digits[i] = 0
		if i == 0:
			digits = [1] + digits
		else:
			digits[i-1] += 1 
		i -= 1
	return digits

ip = [6,9,9,9,9]
print(plusOne(ip))