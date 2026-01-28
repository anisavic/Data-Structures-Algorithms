class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ### CHAT SOLUTION: SLIDING WINDOW DP
        cheapest = 0
        maxProfit = 0
        for price in range(1, len(prices)):
            if prices[price] > prices[cheapest]:
                profit = prices[price] - prices[cheapest]
                maxProfit = max(maxProfit, profit)
            else: #else, update cheapest
                cheapest = price
        return maxProfit

        # minIndex = 0
        # numDecreasing = 0
        # for i in range(len(prices)):
        #     if prices[i] <= prices[minIndex]:
        #         minIndex = i
        #         numDecreasing += 1
        #
        # if numDecreasing == len(prices): #if all decreasing, profit not possible
        #     return 0
        #
        # #now find max
        # maxIndex = minIndex + 1
        # for i in range(maxIndex, len(prices)):
        #     if prices[i] > prices[maxIndex]:
        #         maxIndex = i
        #
        #
        #
        # return prices[maxIndex] - prices[minIndex]

def main():
    s = Solution()
    print(s.maxProfit([2,4,1]))

if __name__ == '__main__':
    main()