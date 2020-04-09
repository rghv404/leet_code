''' Say you have an array prices for which the ith element is the price of a
given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (i.e., buy one and sell one share of the stock
multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you
must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4] Output: 7 Explanation: Buy on day 2 (price = 1) and sell
on day 3 (price = 5), profit = 5-1 = 4. Then buy on day 4 (price = 3) and sell
on day 5 (price = 6), profit = 6-3 = 3. Example 2:

Input: [1,2,3,4,5] Output: 4 Explanation: Buy on day 1 (price = 1) and sell on
day 5 (price = 5), profit = 5-1 = 4. Note that you cannot buy on day 1, buy on
day 2 and sell them later, as you are engaging multiple transactions at the
same time. You must sell before buying again. Example 3:

Input: [7,6,4,3,1] Output: 0 Explanation: In this case, no transaction is
done, i.e. max profit = 0.
 

Constraints:

1 <= prices.length <= 3 * 10 ^ 4 0 <= prices[i] <= 10 ^ 4 '''

# Naivee method is even more complex than I thouhgt, basically for every bit of profit we call the same method recursively
# to calculate how the max value is added over
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        return self.calculateMax(prices, 0)

    def calculateMax(self, num:[int], start:int) -> int:
        globalMax = 0
        if start > len(num) - 1:
            return 0
        for i in range(start, len(num)):
            maxProfit = 0
            for j in range(i+1, len(num)):
                if num[j] > num[i]:
                    profit = num[j] - num[i] + self.calculateMax(num, j+1)
                    maxProfit = max(maxProfit, profit)
                    # print(maxProfit)
            globalMax =  max(globalMax, maxProfit)
        return globalMax

# the other method is the greedy solution where max profit is reached when each spike is accounted for 
# for eg in a scenario as 1, 5, 8 if the user buys at 1 then sells at 8 will give max proft which is equivalent 
# to incremental diff b.w 1 and 5 and 5 and 8 i.e. 4 + 3. Thus greedy and simple

def maxProfit(prices:[int]) -> int:
    maxProfit = 0
    for i in range(1, len(prices)):
        if prices[i-1] < prices[i]:
            maxProfit += prices[i] - prices[i-1]
    return maxProfit

ip = [7,1,5,3,6,4]
res = Solution().maxProfit(ip)
res2 = maxProfit(ip)
print(res, res2)

