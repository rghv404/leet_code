'''
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1

Example 2:

Input: 16
Output: true
Explanation: 24 = 16

Example 3:

Input: 218
Output: false


'''
#  one obvious methos is to keep dividing two until we have eitehr non zero rem or num becomes 1
def isPowerOfTwo(num: int) -> bool:
    if num <= 0:
        return False
    if num == 1:
        return True
    rem = num % 2
    while rem == 0 and num > 2:
        num /= 2
        rem = num % 2
    return False if rem else True


# another methods is to use bitwise and of the number minus one
# cause the power of two number will have only the most significatn bit set to 1 while the one less
# than it will have all of them set except for the most significatn one
# e.g. 8 = 1000 and 7 = 0111 both number bitwise and will give us 0

def isPowerOfTwo_bitWise(num: int) -> bool:
	if num <= 0: return False

	return not(num & (num-1))


print(isPowerOfTwo_bitWise(8))