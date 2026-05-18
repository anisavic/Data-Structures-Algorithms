class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        buy low sell high, return highest profits
        ex: 10,1,5,6,7,1 profit=7-1 (sell) - (buy)
        have to have a buy and a sell, buy index must be smaller
        than sell
        maybe scan through list, keep track of a buy and sell marker,
        making sure buy doesn't pass sell
        have two pointers, buy and sell, go through list
        if price is higher than sell, make new sell
        if price is lower than buy, make new buy
        at the end, return profit if nonegative, otherwise 0


        Bad approach, try lowest price seen so far logic
        [10,1,5,6,7,1]
        lowest = 10
        maximum = 0
        lowest = 10
        lowest = 1
        5-1 = 4 > 0 set maximum = 4
        6-1 = 5 > 4 set maximum to 5
        7-1=6>5 set maximum to 6

        [10,8,7,5,2]
        lowest = 10
        max=0
        lowest = 8
        8-8=0 max = 0

        5,10,1,2
        hold a lowest price and go through, set lower price when you see one, and set the sell if the new profits of selling at that 
        day exceed the maximum profit
        hold lowest_price, set to first elem
        for price in prices:
            if price is lower than lowest, set new

            also if new profits exceed old ones, set new maximum
        """
        lowest = prices[0]
        maximum_profit = 0

        for price in prices:
            #update lowest price seen so far
            lowest = min(price, lowest)

            #update maximum profit seen so far
            current_profits = price - lowest
            maximum_profit = max(current_profits, maximum_profit)
        
        return maximum_profit
            

if __name__ == "__main__":
    t = Solution()
    test = [10,8,7,5,2]
    print(t.maxProfit(test))