'''
Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

 

Example 1:

Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
Output: [null,1,1,1,2,1,4,6]
Explanation: 
First, S = StockSpanner() is initialized.  Then:
S.next(100) is called and returns 1,
S.next(80) is called and returns 1,
S.next(60) is called and returns 1,
S.next(70) is called and returns 2,
S.next(60) is called and returns 1,
S.next(75) is called and returns 4,
S.next(85) is called and returns 6.

Note that (for example) S.next(75) returned 4, because the last 4 prices
(including today's price of 75) were less than or equal to today's price.

 

Note:

    Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
    There will be at most 10000 calls to StockSpanner.next per test case.
    There will be at most 150000 calls to StockSpanner.next across all test cases.
    The total time limit for this problem has been reduced by 75% for C++, and 50% for all other languages.

'''

# my idea is to use a heap , lol no heap can't be used cause even when the array is maintained 
# knowing the index requires another iteration. Best bet is to use bin search 
class StockSpanner:

    def __init__(self):
        self.lst = []

    def next(self, price: int) -> int:
        val = self.binInsert(price)
        print(self.lst, val)

    # helper function to find the position where the element should be inserted
    def binInsert(self, num:int) -> int:
        if not self.lst: # list is empty
            self.lst.append(num)
            return 1
        l, r = 0, len(self.lst) - 1
        while l<r:
            mid = (l+r)//2
            if self.lst[mid] == num: # same element exists, insert either ahead or before
                print(mid)
                while mid < len(self.lst) and self.lst[mid] == num:
                    mid += 1 #this is done cause we need to append at the end of equal subarrays
                insertPos = mid
                # modify array
                print(mid)
                self.lst = self.lst[:insertPos] + [num] + self.lst[insertPos:]
                return insertPos + 1
            elif self.lst[mid] < num: #item to the right
                l = mid + 1
            else:
                r = mid - 1

        # now if the l and r are same and we're out of loop then we need to either insert beofre l or after
        print(l,r)
        if self.lst[l] <= num:
            # insert after
            insertPos = l + 1
        else:
            insertPos = l

        self.lst = self.lst[:insertPos] + [num] + self.lst[insertPos:]
        return insertPos + 1

# above though no doubt is a brilliant solution the question actually needs the consequetive low number adys
# thus it becomes more of a greedy solution where the last max owed is added to current max
class StockSpanner_2:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        weight = 1
        while self.stack and price >= self.stack[-1][0]:
            weight += self.stack.pop()[1]
        self.stack.append((price, weight))
        print(weight, self.stack)
        return weight

obj = StockSpanner_2()
obj.next(100)
obj.next(80)
obj.next(110)
obj.next(110)
obj.next(110)
obj.next(120)
obj.next(115)
obj.next(90)

