''' Perform String Shifts
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.

 

Example 1:

Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation: 
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"
Example 2:

Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:  
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"
 

Constraints:

1 <= s.length <= 100
s only contains lower case English letters.
1 <= shift.length <= 100
shift[i].length == 2
0 <= shift[i][0] <= 1
0 <= shift[i][1] <= 100'''

# find a cumulative shift from teh array and then shif tthe string
import random
def stringShift(s: str, shift: [[int]]) -> str:
	# left is negative and right shift is positive
	cumulativeShift = 0
	for pair in shift:
		direction, amt = pair
		cumulativeShift = cumulativeShift + amt if direction == 1 else cumulativeShift - amt
	# get the shift within the length of string 
	cumulativeShift %= len(s)

	if cumulativeShift > 0:
		# right shift
		return s[len(s)-cumulativeShift:] + s[:len(s)-cumulativeShift]
	else:
		# left shift
		return s[cumulativeShift:] + s[:cumulativeShift]

s = "abcdefgdshfgkdshkfgdsnbkgyrdeiodsh,kvbndfsihytsdkbvskgftiesw"
shift = []
for i in range(100):
	shift.append([random.randint(0, 1), random.randint(0, 100)])
print(shift)
res = stringShift(s, shift)
print(res)
