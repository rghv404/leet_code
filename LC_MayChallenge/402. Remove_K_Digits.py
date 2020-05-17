'''
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:

    The length of num is less than 10002 and will be ≥ k.
    The given num does not contain any leading zero.

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.


'''


def removeKdigits_almost(num: str, k: int) -> str:
	# seems like we can solve it greedily choosing highest bit from first two most significant bit for each removal
    listNum = list(num)
    n = len(listNum)
    if n == k: return "0"
    i = 0
    while i < k and i < len(listNum) - 1:
        if listNum[i] == '0':
            i+=1
            k+=1
            continue
        elif listNum[i] < listNum[i+1]:
            listNum[i], listNum[i+1] = listNum[i+1], listNum[i]
        i += 1
        print(listNum[i:], i)
        
    tempRes = ''.join(listNum[i:])
    if len(tempRes) == 1:
        return tempRes
    # print(tempRes[i:], tempRes[i+1:])
    return tempRes[1:] if tempRes[0]=="0" else tempRes
    # res = ''.join(listNum[i:]) if listNum[i] != '0' and i!=len(listNum[i:]) else ''.join(listNum[i+1:])
    # return res0

# above solutiuon almpst works but fails at cases such as 112 where we need sort of snowballing to determin whic number to remove instead of removing just the left neighbor always
# we keep a stack of numbers for this
def removeKdigits(num: str, k: int) -> str:
	stack, m = [num[0]], 0
	
	if k >= len(num):return "0"

	for i in range(1, len(num)):
		while m < k and stack and num[i] < stack[-1]:
			stack.pop()
			m += 1
		if not stack and num[i] == "0": continue
		stack.append(num[i])

	# it is possible that for monotonically increasing string we have not remove all required number in above loop
	# thus we remove k - m digits from left (cause biggest in left in mono inc num)
	while (k - m) > 0:
		stack.pop()
		m += 1

	if not stack:
		return "0"

	return ''.join(stack)


arr = "42305"
arr = "1102"
res = removeKdigits(arr, 2)
print(res)



