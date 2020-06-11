'''
Original dp problem to find min # of coins to get a desired amount
Assuming we can have infinite number of a particular coins
'''

def minCoinsForSum(coins:[int], amount:int) -> int:
	dp = [float('inf') for i in range(amount+1)]
	dp[0] = 0 # i.e. 0 min coins of den. 0 to get 0 sum... lel

	for coin in coins:
		for currAmt in range(len(dp)):
			if currAmt >= coin:
				# the logic is simple the value will be either the already populated value (min # to reach currAmt from prev Coin)
				# or min value of currAmt - coin plus the 1  (which is current coin contribution)
				dp[currAmt] = min(dp[currAmt], dp[currAmt - coin] + 1)
	return dp[amount]


ip = [2,3]
amt = 900
res = minCoinsForSum(ip, amt)
print(res)
