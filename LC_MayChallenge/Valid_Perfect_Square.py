'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true

Example 2:

Input: 14
Output: false

'''

# one method is to use linear search from 1 to n until i*i <=n. works in o(n) time
# another method is to use binary search to do the above searching
def isPerfectSquare_bin(num: int) -> bool:
	l = 0
	r = num
	while l<=r:
		mid = (l+r)//2
		if mid*mid > n:
			r = mid - 1
		elif mid*mid < n:
			l = mid + 1
		else:
			return True
	return False

# interestingly you dont;' have to keep the upper bbound as num cause anything more than half of num will never be the sqrt. Half is laso only possible of 4
def isPerfectSquare(num: int) -> bool:
	if num < 2:
        return True
    l = 2
    r = num // 2
    while l<=r:
        mid = (l+r)//2
        if mid*mid > num:
            r = mid - 1
        elif mid*mid < num:
            l = mid + 1
        else:
            return True
    return False


n = 289
res = isPerfectSquare(n)
print(res)
