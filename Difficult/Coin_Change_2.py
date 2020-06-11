'''
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

 

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:

Input: amount = 10, coins = [10] 
Output: 1

 

Note:

You can assume that

    0 <= amount <= 5000
    1 <= coin <= 5000
    the number of coins is less than 500
    the answer is guaranteed to fit into signed 32-bit integer


'''
class Solution:
	def __init__(self):
		self.res = 0

	def helper(self, currSum: int, total: int, coins: [int], start: int):
		if currSum == total:
			self.res += 1
			return

		for i in range(start, len(coins)):
			num = coins[i]
			if num + currSum > total:
				# print('Excceds: ', num, currSum)
				# print('res while exceeding, ', self.res)
				break
			self.helper(num+currSum, total, coins, i)

	def change(self, amount: int, coins: [int]) -> int:	
		coins.sort()
		self.helper(0, amount, coins, 0)
		print(self.res)


# well above solution defnitely wokrs but time limit exceeds cause of it's P(amt**n) time complexity
# cause of n coins choices (we can repeatedly take as many) and which can go upto amt number

# we can use dynamic programming here to calculate the ways in which coins can be selected
def change(coins:[int], amount:int) -> int:
	# have a one dimensional array indicating the sum we are trying to get
	arr = [0 for _ in range(amount+1)]
	arr[0] = 1 # indicate that to acheive 0 amount 1 way exists (select no coin ;)
	# loop through coins at level 1 and then sum at level 2
	print(arr, len(arr))
	for coin in coins:
		for currAmt in range(amount+1):
			# only conside when the coin values is greater equal to amount we want
			if currAmt >= coin:
				arr[currAmt] += arr[currAmt - coin]
		print(arr)
	return arr[amount]


ip = [1,2,5]
ip = [10]
amt = 10
obj = Solution()
obj.change(amt, ip)
res = change(ip, amt)
print(res)

